from django.shortcuts import render
from django.http import JsonResponse
from .fcsxapi import get_market_price, get_historic_data

def market_price(request):
    data = get_market_price()
    return JsonResponse({"data": data})

def historic_data(request):
    data = get_historic_data()
    return JsonResponse({"data": data})