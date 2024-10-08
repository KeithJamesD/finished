import streamlit as st
import pandas as pd
import requests
from pandas import json_normalize
import creds

st.set_page_config(layout="wide")

# Create website template with input trigger for code 
st.markdown("<h1 style='text-align: center; color: green;'>Quant Web App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: grey;'>NASDAQ Stock Evaluator</h2>", unsafe_allow_html=True)

# Load NASDAQ listed stocks from CSV
nasdaq_stocks = pd.read_csv('nasdaq_screener.csv')
stock_symbols = nasdaq_stocks['Symbol'].tolist()

# Function to fetch stock data from FMP API
def fetch_stock_data(symbol):
    url_quote = f'https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={creds.api_key}'
    url_dcf = f'https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}?apikey={creds.api_key}'
    url_metrics = f'https://financialmodelingprep.com/api/v3/key-metrics-ttm/{symbol}?apikey={creds.api_key}'
    
    response_quote = requests.get(url_quote)
    response_dcf = requests.get(url_dcf)
    response_metrics = requests.get(url_metrics)
    
    data_quote = response_quote.json()
    data_dcf = response_dcf.json()
    data_metrics = response_metrics.json()
    
    if data_quote and data_dcf and data_metrics:
        quote = json_normalize(data_quote)
        dcf = json_normalize(data_dcf)
        metrics = json_normalize(data_metrics)
        
        if not quote.empty and not dcf.empty and not metrics.empty:
            current_price = quote['price'].iloc[0]
            dcf_value = dcf['dcf'].iloc[0]
            pe_ratio = metrics.get('peRatioTTM', [None])[0]  # Use .get() to safely access the key
            intrinsic_value = current_price / dcf_value
            return symbol, current_price, dcf_value, intrinsic_value, pe_ratio
    return None

# User input for PE ratio filter
pe_ratio_min = st.sidebar.number_input("Min PE Ratio", value=0)
pe_ratio_max = st.sidebar.number_input("Max PE Ratio", value=25)

# Filter stocks based on criteria
filtered_stocks = []
for symbol in stock_symbols:
    stock_data = fetch_stock_data(symbol)
    if stock_data:
        symbol, current_price, dcf_value, intrinsic_value, pe_ratio = stock_data
        if current_price < 50 and intrinsic_value < 1 and pe_ratio is not None and pe_ratio_min <= pe_ratio <= pe_ratio_max:
            filtered_stocks.append(stock_data)

# Create DataFrame for filtered stocks
df_filtered_stocks = pd.DataFrame(filtered_stocks, columns=['Symbol', 'Price', 'DCF', 'Intrinsic Value', 'PE Ratio'])

# Display the filtered stocks
st.write("Stocks with Price < $50, Intrinsic Value < 1, and PE Ratio within specified range")
st.dataframe(df_filtered_stocks)