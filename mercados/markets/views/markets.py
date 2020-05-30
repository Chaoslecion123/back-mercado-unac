# DJANGO REST FRAMEWORK
from rest_framework import viewsets, status, filters,mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# DJANGO
from django.shortcuts import render

# Model
from mercados.markets.models import Market


#Serializers
from markets.serializers.markets import MarketSerializer

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')


