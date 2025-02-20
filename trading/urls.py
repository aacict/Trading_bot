from django.urls import path
from .views import market_price

urlpatterns = [
    path("pair-price/", market_price, name="market-price"),
]
