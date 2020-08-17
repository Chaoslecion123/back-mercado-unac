#PYTHON
import requests
import base64
import pytz

#utilities
from datetime import datetime


# DJANGO REST FRAMEWORK
from rest_framework import viewsets, status,mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.views import APIView


# DJANGO
from django.conf import settings
from django.shortcuts import render
from django.views.generic import DetailView
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from django.db import transaction
from django.db.models import Q




# Model
from mercados.markets.models import Market,MarketPassRequest,CounterMarket
from mercados.schedule.models import Schedule
from mercados.clients.models import Client


#Serializers
from markets.serializers.markets import MarketSerializer,CounterMarketSerializer,MarketPassRequestSerializer
from mercados.schedule.serializers.schedule import ScheduleSerializer

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filter_fields = [
        'address__country_area__name',
        'address__city__name',
        'address__city_area__name', 
        'name'          
    ]
    search_fields = [
        'address__line_1',
        'name',
        'address__country_area__name',
        'address__city__name',
        'address__city_area__name', 
    ]
    ordering_fields = [
        'name'
    ]	
    
    @action(
        detail=True,
        methods=['get']
    )
    def horarios(self,request,pk=None):
        object_ = self.get_object()
        schedules=Schedule.objects.filter(markets=object_)
        return Response(ScheduleSerializer(schedules,many=True).data)



    @action(
        detail=True,
        methods=['get']
    )
    def counter_market(self,request,pk=None):
        object_ = self.get_object()
        counter_market=CounterMarket.objects.filter(markets=object_)
        return Response(CounterMarketSerializer(counter_market,many=True).data)


class CounterMarketViewSet(viewsets.ModelViewSet):
    queryset = CounterMarket.objects.all()
    serializer_class = CounterMarketSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filter_fields = [
           
    ]
    search_fields = [
     'markets',
     'count_aforo'
    ]
    ordering_fields = [
        
    ]


    # def generate_pdf(request,id_):
    #     print('--- --- ---')
    #     print(id_)
    #     print('--- --- ---')
    #     url_pdf = "%s/documento/%s/pdf" % (settings.API_URL,id_)
    #     r = requests.get(url_pdf)
        
    #     with open("/tmp/%s_pdf.pdf" % id_, "wb") as f:
    #         f.write(r.content)

    #     with open("/tmp/%s_pdf.pdf" % id_, "rb") as pdf_file:
    #         encoded_string = base64.b64encode(pdf_file.read())

    #     return encoded_string

    @action(
        detail=True,
        methods=['get']
    )
    def generate_pass(self,request,pk=None):
        object_ = self.get_object()
        market = object_.markets

        #counter_market = CounterMarket.objects.filter(pk=pk).first()
       
        market_request_pass =  MarketPassRequest.objects.filter(counter_market=object_).exists()
        if object_.count_aforo < market.aforo:
            with transaction.atomic(): 
                cliente = Client.objects.get(pk=1)
                
                object_.count_aforo += 1
                object_.save()
                
            market_pass_request = MarketPassRequest()
            market_pass_request.counter_market = object_
            market_pass_request.count = object_.count_aforo
            market_pass_request.client = cliente
            market_pass_request.save()
            
            url_pdf = "{}/documento/{}/pdf/".format(settings.API_URL,object_.id)

            print('--- --- ---')
            print(type(url_pdf))
            print('--- --- ---')

            r = requests.get(url_pdf)

            
            
            with open("/tmp/%s_pdf.pdf" % object_.id, "wb") as f:
                f.write(r.content)
                

            with open("/tmp/%s_pdf.pdf" % object_.id, "rb") as pdf_file:
                encoded_string = base64.b64encode(pdf_file.read())

            market_pass_request.archivopdf = encoded_string
            market_pass_request.save()

            data = {'pdf': market_pass_request.archivopdf,'name': market.name}
            return Response(data, status=status.HTTP_200_OK)
        else :
            return Response({
                'ok':False,
                counter_market.schedule: 'foro lleno'
            })

    @action(methods=['get'], detail=True)
    def pdf(self, request, pk=None):
        invoice = self.get_object()
        data = {'pdf': "%s" % invoice.market_pass_requests.first().archivopdf, 'name': "%s" % 'fernandito'}
        return Response(data, status=status.HTTP_200_OK)


class MarketPassRequestViewSet(viewsets.ModelViewSet):
    queryset = MarketPassRequest.objects.all()
    serializer_class = MarketPassRequestSerializer

    def create(self, request, *args, **kwargs):
        id_counter_market = request.data["id_counter_market"]
        name_schedule = request.data["name_schedule"]
        user_id = request.data["user_id"]

        cliente = Client.objects.get(pk=user_id)

        if cliente.users_client.exists():
            
            ultimo_pase_generado = cliente.users_client.last().counter_market

            hora_inicial_ultimo_pase_generado = ultimo_pase_generado.schedule.time_start.strftime('%H:%M')
            hora_final_ultimo_pase_generado = ultimo_pase_generado.schedule.time_end.strftime('%H:%M')
            hora_actual = datetime.now(pytz.timezone('America/Lima')).strftime("%H:%M")


            if hora_actual >= hora_inicial_ultimo_pase_generado and hora_actual <= hora_final_ultimo_pase_generado :
                data = {
                    'ok':False,
                    'message':'El tiempo de tu pase todavia no caduca.'
                }
                return Response(data, status=status.HTTP_200_OK)
  
            else:
                counter_market = CounterMarket.objects.filter(Q(id=id_counter_market)).last()
                market = counter_market.markets


                hora_salida_final = counter_market.schedule.time_end.strftime('%H:%M')
                hora_entrada = counter_market.schedule.time_start.strftime('%H:%M')
                

        
                if hora_entrada and (hora_actual > hora_salida_final):
                    if counter_market.count_aforo < market.aforo:
                        with transaction.atomic():

                            
                            counter_market.count_aforo += 1
                            
                            market_pass_request = MarketPassRequest()
                            market_pass_request.counter_market = counter_market
                            market_pass_request.count = counter_market.count_aforo
                            market_pass_request.client = cliente

                            counter_market.save()

                            market_pass_request.save()


                        informacion = {
                            'market_pass_request_id':market_pass_request.id,
                        }
                        return Response(informacion, status=status.HTTP_200_OK)
                    else: 
                        data = {
                            'ok':False,
                            'message':'foro del mercado lleno'
                        }
                        return Response(data, status=status.HTTP_200_OK)
                else:
                    data = {
                        'ok':False,
                        'message':'El tiempo de tu pase todavia no caduca.'
                    }
                    return Response(data, status=status.HTTP_200_OK)
        else:
            
            counter_market = CounterMarket.objects.filter(Q(id=id_counter_market)).last()
            market = counter_market.markets
            markets_pass_request = cliente.users_client.last()

            hora_salida_final = counter_market.schedule.time_end.strftime('%H:%M')
            hora_entrada = counter_market.schedule.time_start.strftime('%H:%M')
            hora_actual = datetime.now(pytz.timezone('America/Lima')).strftime("%H:%M") 

            if hora_actual > hora_salida_final:
                data = {
                    'ok':False,
                    'message':'este horario ya no esta disponible'
                }
                return Response(data, status=status.HTTP_200_OK)
            
            else:

                if counter_market.count_aforo < market.aforo:
                    
                    with transaction.atomic():

                        
                        counter_market.count_aforo += 1
                        
                        market_pass_request = MarketPassRequest()
                        market_pass_request.counter_market = counter_market
                        market_pass_request.count = counter_market.count_aforo
                        market_pass_request.client = cliente

                        counter_market.save()

                        market_pass_request.save()


                    informacion = {
                        'market_pass_request_id':market_pass_request.id,
                    }
                    return Response(informacion, status=status.HTTP_200_OK)
                else: 
                    data = {
                        'ok':False,
                        'message':'foro del mercado lleno'
                    }
                    return Response(data, status=status.HTTP_200_OK)


    @action(methods=['get'], detail=True)
    def pdf(self, request, pk=None):
        invoice = self.get_object()
        data = {
            'pdf': invoice.id,
            'mercado': invoice.counter_market.markets.name,
            'nro_pase':invoice.count,
            'direccion_1':invoice.counter_market.markets.address.line_1,
            'direccion_2':invoice.counter_market.markets.address.line_2,
            'nombre_completo': f'{invoice.client.first_name} {invoice.client.last_name}',
            'dni': f'{invoice.client.dni}',
            'name':'fernandito',
            'horario': f'{invoice.counter_market.schedule}',
            'horario_inicio': invoice.counter_market.schedule.time_start,
            'horario_fin':invoice.counter_market.schedule.time_end
        }
        return Response(data, status=status.HTTP_200_OK)


class DocumentoPDFView(PDFTemplateResponseMixin, DetailView):
    model = CounterMarket
    template_name = "documentos/pase.html"
    context_object_name = 'documento'

    def get_context_data(self,**kwargs):
        return super().get_context_data(
            pagesize="A4",
            title="{}.pdf".format(self.get_object()),
            encoding=u"utf-8",
            pdf_filename="DOCUMENTO",
            **kwargs
        )


    