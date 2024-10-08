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
    urls = {
        "quote": f'https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={creds.api_key}',
        "dcf": f'https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}?apikey={creds.api_key}',
        "metrics": f'https://financialmodelingprep.com/api/v3/key-metrics-ttm/{symbol}?apikey={creds.api_key}'
    }

    data = {key: fetch_data(url) for key, url in urls.items()}

    if all(data.values()):
        quote = json_normalize(data['quote'])
        dcf = json_normalize(data['dcf'])
        metrics = json_normalize(data['metrics'])

        if not quote.empty and not dcf.empty and not metrics.empty:
            current_price = quote.get('price', [None])[0]
            dcf_value = dcf.get('dcf', [None])[0]
            pe_ratio = metrics.get('peRatioTTM', [None])[0]
            ps_ratio = metrics.get('priceToSalesRatioTTM', [None])[0]
            pb_ratio = metrics.get('priceToBookRatioTTM', [None])[0]
            peg_ratio = metrics.get('pegRatioTTM', [None])[0]
            de_ratio = metrics.get('debtEquityRatioTTM', [None])[0]
            intrinsic_value = current_price / dcf_value if current_price and dcf_value else None

            return symbol, current_price, dcf_value, intrinsic_value, pe_ratio, ps_ratio, pb_ratio, peg_ratio, de_ratio

    return None
# User input for PE ratio filter
pe_ratio_min = st.sidebar.number_input("Min PE Ratio", value=0)
pe_ratio_max = st.sidebar.number_input("Max PE Ratio", value=25)

# User input for additional filters
ps_filter_1 = st.sidebar.checkbox("PS < 1")
ps_filter_2 = st.sidebar.checkbox("PS < 2")
pb_filter_1 = st.sidebar.checkbox("PB < 1")
pb_filter_2 = st.sidebar.checkbox("PB < 2")
peg_filter_1 = st.sidebar.checkbox("PEG < 1")
peg_filter_2 = st.sidebar.checkbox("PEG < 2")
de_filter_1 = st.sidebar.checkbox("DE < 1")
de_filter_2 = st.sidebar.checkbox("DE < 2")

# Filter stocks based on criteria
filtered_stocks = []
for symbol in stock_symbols:
    stock_data = fetch_stock_data(symbol)
    if stock_data:
        symbol, current_price, dcf_value, intrinsic_value, pe_ratio, ps_ratio, pb_ratio, peg_ratio, de_ratio = stock_data
        if current_price is not None and current_price < 50 and intrinsic_value is not None and intrinsic_value < 1 and pe_ratio is not None and pe_ratio_min <= pe_ratio <= pe_ratio_max:
            if (not ps_filter_1 or (ps_ratio is not None and ps_ratio < 1)) and \
               (not ps_filter_2 or (ps_ratio is not None and ps_ratio < 2)) and \
               (not pb_filter_1 or (pb_ratio is not None and pb_ratio < 1)) and \
               (not pb_filter_2 or (pb_ratio is not None and pb_ratio < 2)) and \
               (not peg_filter_1 or (peg_ratio is not None and peg_ratio < 1)) and \
               (not peg_filter_2 or (peg_ratio is not None and peg_ratio < 2)) and \
               (not de_filter_1 or (de_ratio is not None and de_ratio < 1)) and \
               (not de_filter_2 or (de_ratio is not None and de_ratio < 2)):
                filtered_stocks.append(stock_data)

# Create DataFrame for filtered stocks
df_filtered_stocks = pd.DataFrame(filtered_stocks, columns=['Symbol', 'Price', 'DCF', 'Intrinsic Value', 'PE Ratio', 'PS Ratio', 'PB Ratio', 'PEG Ratio', 'DE Ratio'])

# User input for PE ratio filter
pe_ratio_min = st.sidebar.number_input("Min PE Ratio", value=0)
pe_ratio_max = st.sidebar.number_input("Max PE Ratio", value=25)

# User input for additional filters
ps_filter_1 = st.sidebar.checkbox("PS < 1")
ps_filter_2 = st.sidebar.checkbox("PS < 2")
pb_filter_1 = st.sidebar.checkbox("PB < 1")
pb_filter_2 = st.sidebar.checkbox("PB < 2")
peg_filter_1 = st.sidebar.checkbox("PEG < 1")
peg_filter_2 = st.sidebar.checkbox("PEG < 2")
de_filter_1 = st.sidebar.checkbox("DE < 1")
de_filter_2 = st.sidebar.checkbox("DE < 2")

# Filter stocks based on criteria
filtered_stocks = []
for symbol in stock_symbols:
    stock_data = fetch_stock_data(symbol)
    if stock_data:
        symbol, current_price, dcf_value, intrinsic_value, pe_ratio, ps_ratio, pb_ratio, peg_ratio, de_ratio = stock_data
        if current_price is not None and current_price < 50 and intrinsic_value is not None and intrinsic_value < 1 and pe_ratio is not None and pe_ratio_min <= pe_ratio <= pe_ratio_max:
            if (not ps_filter_1 or (ps_ratio is not None and ps_ratio < 1)) and \
               (not ps_filter_2 or (ps_ratio is not None and ps_ratio < 2)) and \
               (not pb_filter_1 or (pb_ratio is not None and pb_ratio < 1)) and \
               (not pb_filter_2 or (pb_ratio is not None and pb_ratio < 2)) and \
               (not peg_filter_1 or (peg_ratio is not None and peg_ratio < 1)) and \
               (not peg_filter_2 or (peg_ratio is not None and peg_ratio < 2)) and \
               (not de_filter_1 or (de_ratio is not None and de_ratio < 1)) and \
               (not de_filter_2 or (de_ratio is not None and de_ratio < 2)):
                filtered_stocks.append(stock_data)

# Create DataFrame for filtered stocks
df_filtered_stocks = pd.DataFrame(filtered_stocks, columns=['Symbol', 'Price', 'DCF', 'Intrinsic Value', 'PE Ratio', 'PS Ratio', 'PB Ratio', 'PEG Ratio', 'DE Ratio'])