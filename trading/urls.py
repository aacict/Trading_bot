from django.urls import path
from .views import market_price, historic_data

urlpatterns = [
    path("pair-price/", market_price, name="market-price"),
    path("historic-price/", historic_data, name="historic-price"),
]
