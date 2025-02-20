import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
API_URL = "http://127.0.0.1:8000/api/historic-price/"

def fetch_price():
    response = requests.get(API_URL)
    print(".........................response", response.json())
    return response.json()["data"]

data = fetch_price()

# Convert data to a pandas DataFrame
df = pd.DataFrame.from_dict(data["response"], orient='index')

# Convert Unix time to datetime
df['time'] = pd.to_datetime(df['t'], unit='s')

# Convert 'open', 'high', 'low', 'close' from string to float
df['open'] = df['o'].astype(float)
df['high'] = df['h'].astype(float)
df['low'] = df['l'].astype(float)
df['close'] = df['c'].astype(float)

# Plot the candlestick chart using Plotly
fig = go.Figure(data=[go.Candlestick(
    x=df['time'],
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close'],
    name="Candlestick"
)])

# Customize the layout
fig.update_layout(
    title="Forex/Stock Trading Candlestick Chart",
    xaxis_title="Date",
    yaxis_title="Price",
    xaxis_rangeslider_visible=False  # Disable the range slider
)

# Streamlit app display
st.title("Trading Dashboard")
st.plotly_chart(fig)

