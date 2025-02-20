import time
import hmac
import hashlib
import requests
from django.conf import settings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

FCSAPIKEY = os.getenv("FCSAPIKEY")
FCSAPIBASEENDPOINT = os.getenv("FCSAPIBASEENDPOINT")

# Generate request headers for authentication
def get_headers(method, request_path, body=""):
    timestamp = str(int(time.time() * 1000))

    return {
        "ACCESS-KEY": FCSAPIKEY,
        "ACCESS-TIMESTAMP": timestamp,
        "Content-Type": "application/json",
    }

# Fetch latest market price
def get_market_price(id=1, symbol="EUR/USD"):
    url = f"{FCSAPIBASEENDPOINT}/latest?id={id}&access_key={FCSAPIKEY}&symbol={symbol}"
    response = requests.get(url, headers=get_headers("GET", "/latest"))
    print(".........................response", response.json())
    return response.json()

# Fetch historic data
def get_historic_data(id=1, level=3, period="1h", symbol="EUR/USD"):
    url = f"{FCSAPIBASEENDPOINT}/history?symbol={symbol}&access_key={FCSAPIKEY}&level={level}&period={period}"
    response = requests.get(url, headers=get_headers("GET", "/latest"))
    print(".........................response", response.json())
    return response.json()