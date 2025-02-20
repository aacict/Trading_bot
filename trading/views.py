from django.shortcuts import render
from django.http import JsonResponse
from .fcsxapi import get_market_price

def market_price(request):
    """API Endpoint to get the latest market price."""
    price = get_market_price()
    return JsonResponse({"price": price})