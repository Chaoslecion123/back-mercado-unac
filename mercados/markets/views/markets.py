# DJANGO REST FRAMEWORK
from rest_framework import viewsets, status,mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

# DJANGO
from django.shortcuts import render
from django.views.generic import DetailView
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin


# Model
from mercados.markets.models import Market


#Serializers
from markets.serializers.markets import MarketSerializer

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

           
    ]
    search_fields = [
        'name'
    ]
    ordering_fields = [
        'name'
    ]
    

    @action(
        detail=True,
        methods=['post']
    )
    def solicitar_pase(self,request,pk=None):
        print('**** **** ***')
        print(self.get_object().count_aforo)
        print('**** **** ***')
        object_ = self.get_object()
        if object_.count_aforo >= object_.aforo:
            data =  {
               'message': 'aforo lleno' 
            }
            return Response(data)
        else:
            object_.count_aforo += 1
            object_.save()

            return Response({
                'pase': object_.count_aforo,
                'mercado': object_.name,
                'direccion': object_.address.line_1,
                'message': 'el aforo no esta lleno'
            })

    

class DocumentoPDFView(PDFTemplateResponseMixin, DetailView):
    model = Market
    template_name = "documentos/pase.html"
    context_object_name = 'documento'

    def get_context_data(self,**kwargs):
        return super().get_context_data(
            pagesize="A4",
            title="{}.pdf".format(self.get_object().name),
            encoding=u"utf-8",
            pdf_filename="DOCUMENTO",
            **kwargs
        )

        