import requests
import pandas as pd
import numpy as np
import streamlit as st
from pandas import json_normalize
import creds

st.set_page_config(layout="wide")

# Create website template with input trigger for code 
st.markdown("<h1 style='text-align: center; color: green;'>MacGuffin</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: grey;'>Stock Evaluator</h2>", unsafe_allow_html=True)

symbol = st.sidebar.text_input("TICKER", "AAPL")

reqk = requests.get(f'https://financialmodelingprep.com/api/v3/key-metrics-ttm/{symbol}?&apikey={creds.api_key}')
datak = reqk.json()
k = json_normalize(datak)
dfk = pd.DataFrame(k)

BOOK = dfk['bookValuePerShareTTM'].iloc[0]


# Fetch discounted cash flow (DCF)
req_dcf = requests.get(f'https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}?apikey={creds.api_key}')
data_dcf = req_dcf.json()
dcf = json_normalize(data_dcf)
df_dcf = pd.DataFrame(dcf)

# Fetch current price
req_quote = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={creds.api_key}')
data_quote = req_quote.json()
quote = json_normalize(data_quote)
df_quote = pd.DataFrame(quote)

# Check if data is available
if not df_dcf.empty and not df_quote.empty:
    current_price = df_quote['price'].iloc[0]
    dcf_value = df_dcf['dcf'].iloc[0]
    intrinsic_value = current_price / dcf_value
else:
    current_price = None
    dcf_value = None
    intrinsic_value = None

# Display the values
#if current_price is not None and dcf_value is not None:
    #st.write(f"Current Price: ${current_price}")
    #st.write(f"Discounted Cash Flow (DCF): ${dcf_value}")
    #st.write(f"Intrinsic Value: ${intrinsic_value}")
#else:
    #st.write("Data not available for the selected stock.")

#fetch ratios
req = requests.get(f'https://financialmodelingprep.com/api/v3/ratios-ttm/{symbol}?&apikey={creds.api_key}')
data = req.json()
ratiosTTM = json_normalize(data)
dfratiosTTM = pd.DataFrame(ratiosTTM)

#get required ratios
PEG = dfratiosTTM['pegRatioTTM'].iloc[0]
PE = dfratiosTTM['peRatioTTM'].iloc[0]
P2B = dfratiosTTM['priceToBookRatioTTM'].iloc[0]
P2S = dfratiosTTM['priceToSalesRatioTTM'].iloc[0]
DE = dfratiosTTM['debtEquityRatioTTM'].iloc[0]
DECAPEX = dfratiosTTM['longTermDebtToCapitalizationTTM'].iloc[0]
OCFPS = dfratiosTTM['operatingCashFlowPerShareTTM'].iloc[0]
FCF = dfratiosTTM['freeCashFlowPerShareTTM'].iloc[0]
P2FCF = dfratiosTTM['payoutRatioTTM'].iloc[0]
CPS = dfratiosTTM['cashPerShareTTM'].iloc[0]
DIV = dfratiosTTM['dividendYielTTM'].iloc[0]
DIVPAID = dfratiosTTM['dividendPerShareTTM'].iloc[0]
ROE = dfratiosTTM['returnOnEquityTTM'].iloc[0]
CURRENT = dfratiosTTM['currentRatioTTM'].iloc[0]
QUICK = dfratiosTTM['quickRatioTTM'].iloc[0]
PO = dfratiosTTM['payoutRatioTTM'].iloc[0]
ROA = dfratiosTTM['returnOnAssetsTTM'].iloc[0]


#PEG
peg_tbl=pd.DataFrame({
    'PEG Ratio':[PEG]
})


peg_tbl = pd.melt(peg_tbl)

#DEBT
debt_tbl=pd.DataFrame({
    'Debt to Equity':[DE],
    'Debt to Capitalization':[DECAPEX]
})

debt_tbl = pd.melt(debt_tbl)

#VALUE
value_tbl=pd.DataFrame({
    'Price to Earnings':[PE],
    'Price to Sales':[P2S],
    'Price to Book':[P2B]
})

value_tbl_tbl = pd.melt(value_tbl)

#Dividends
div_tbl=pd.DataFrame({
    'Dividend Yield':[DIV],
    'Dividend':[DIVPAID],
    'Return on Equity':[ROE],
    'Return on Assets':[ROA],
    'Return on Equity':[ROE],
    'Return on Assets':[ROA]
})

div_tbl = pd.melt(div_tbl)

#CASH
cash_tbl=pd.DataFrame({
    'Cash per Share':[CPS],
    'Operating Cash Flow per Share':[OCFPS],
    'Free Cash Flow per Share':[FCF]
})

cash_tbl = pd.melt(cash_tbl)

#BASICS
basic_tbl=pd.DataFrame({
    'Current Ratio':[CURRENT],
    'Quick Ratio':[QUICK],
    'Payout Ratio':[PO]
})

basic_tbl = pd.melt(basic_tbl)

#another required df; repeat as necessary
req2 = requests.get(f'https://financialmodelingprep.com/api/v3/profile/{symbol}?&apikey={creds.api_key}')
data2 = req2.json()
profile = json_normalize(data2)
dfprofile = pd.DataFrame(profile)

#print(dfprofile.head())

MCAP=dfprofile['mktCap'].iloc[0]
NAME=dfprofile['companyName'].iloc[0]
EXCHANGE=dfprofile['exchangeShortName'].iloc[0]
SECTOR=dfprofile['sector'].iloc[0]
INDUSTRY=dfprofile['industry'].iloc[0]


dfprofile_tbl1=pd.DataFrame({
    "Company":[NAME],
    "Market Cap":[MCAP],
    "Exchange":[EXCHANGE]
})

dfprofile_tbl2=pd.DataFrame({
    "Sector":[SECTOR],
    "Industry":[INDUSTRY]
})

req3 = requests.get(f'https://financialmodelingprep.com/api/v3/financial-growth/{symbol}?&apikey={creds.api_key}')
data3 = req3.json()
growth = json_normalize(data3)
dfgrowth = pd.DataFrame(growth)

REVG = dfgrowth['revenueGrowth'].iloc[0]
REVG3 = dfgrowth['threeYRevenueGrowthPerShare'].iloc[0]
REVG5 = dfgrowth['fiveYRevenueGrowthPerShare'].iloc[0]
REVG10 = dfgrowth['tenYRevenueGrowthPerShare'].iloc[0]
NETINCG = dfgrowth['netIncomeGrowth'].iloc[0]
NETINCG3 = dfgrowth['threeYNetIncomeGrowthPerShare'].iloc[0]
NETINCG5 = dfgrowth['fiveYNetIncomeGrowthPerShare'].iloc[0]
NETINCG10 = dfgrowth['tenYNetIncomeGrowthPerShare'].iloc[0]
DATE = dfgrowth['date'].iloc[0]
EPSG = dfgrowth['epsgrowth'].iloc[0]


dfgeps_tbl=pd.DataFrame({
    "Date":[DATE],
    "Revenue Growth":[REVG],
    "Net Income Growth":[NETINCG],
    "EPS Growth":[EPSG]

})

dfgrev_tbl=pd.DataFrame({
    "Date":[DATE],
    "3 Year Revenue Growth":[REVG3],
    "5 Year Revenue Growth":[REVG5],
    "10 Year Revenue Growth":[REVG10]
})

dfginc_tbl=pd.DataFrame({
    "Date":[DATE],
    "3 Year Net Income Growth":[NETINCG3],
    "5 Year Net Income Growth":[NETINCG5],
    "10 Year Net Income Growth":[NETINCG10]
})


req5 = requests.get(f'https://financialmodelingprep.com/api/v3/technical_indicator/5min/{symbol}?type=rsi&period=14&apikey={creds.api_key}')
data5 = req5.json()
rsi = json_normalize(data5)
dfrsi = pd.DataFrame(rsi)

DATE = dfrsi['date'].iloc[0]
RSI = dfrsi['rsi'].iloc[0]

RSI = np.mean(RSI)

req7 = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{symbol}?&apikey={creds.api_key}')
data7 = req7.json()
quote = json_normalize(data7)
dfquote = pd.DataFrame(quote)

PRICE = dfquote['price'].iloc[0]
VOLUME = dfquote['volume'].iloc[0]
CHANGE = dfquote['changesPercentage'].iloc[0]

quote_tbl=pd.DataFrame({
    "Price":[PRICE],
    "Volume":[VOLUME],
    "Percent Change":[CHANGE]
})

EPS = PRICE/PE

quote_tbl = pd.melt(quote_tbl)

req8 = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{symbol}?period=annual&apikey={creds.api_key}')
data8 = req8.json()
income = json_normalize(data8)
dfincome = pd.DataFrame(income)

REVENUE = dfincome['revenue'].iloc[0]
COSTREVENUE = dfincome['costOfRevenue'].iloc[0]
GROSSPROFIT = dfincome['grossProfit'].iloc[0]
GROSSPROFITMARGIN = dfincome['grossProfitRatio'].iloc[0]
RESEARCH = dfincome['researchAndDevelopmentExpenses'].iloc[0]
DEPRECIATION = dfincome['depreciationAndAmortization'].iloc[0]
SGA = dfincome['sellingGeneralAndAdministrativeExpenses'].iloc[0]
OPERATINGEXPENSES = dfincome['operatingExpenses'].iloc[0]
COSTS = dfincome['costAndExpenses'].iloc[0]
INTEREST = dfincome['interestExpense'].iloc[0]
INCB4TAX = dfincome['incomeBeforeTax'].iloc[0]
INCTAXPAID = dfincome['incomeTaxExpense'].iloc[0]
DATE2 = dfincome['date'].iloc[0]


dfcosts_tbl=pd.DataFrame({
    "Date":[DATE2],
    "Research and Development":[RESEARCH],
    "Depreciation and Amortization":[DEPRECIATION],
    "Selling, General and Administrative":[SGA],
    "Interest":[INTEREST],
    "Income Tax Paid":[INCTAXPAID],
    "Total Expenses":[COSTS]
})

dfrev_tbl=pd.DataFrame({                                                                                                                                
    "Date":[DATE2],                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    "Revenue":[REVENUE],
    "Income Before Tax":[INCB4TAX],
    "Cost of Revenue":[COSTREVENUE]
})

dfprofit_tbl=pd.DataFrame({
    "Date":[DATE2],
    "Gross Profit":[GROSSPROFIT],
    "Gross Profit Margin":[GROSSPROFITMARGIN]
})

NetEarnings = REVENUE -(DEPRECIATION + INTEREST + INCTAXPAID + COSTS)


req9 = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}?period=annual&apikey={creds.api_key}')
data9 = req9.json()
assets = json_normalize(data9)
dfassets = pd.DataFrame(assets)

CASH = dfassets['cashAndCashEquivalents'].iloc[0]
ASSETS = dfassets['totalCurrentAssets'].iloc[0]
SHORTDEBT = dfassets['shortTermDebt'].iloc[0]
LONGDEBT = dfassets['longTermDebt'].iloc[0]
LIABILITIES = dfassets['totalCurrentLiabilities'].iloc[0]
RECEIVABLES = dfassets['netReceivables'].iloc[0]
INVENTORY = dfassets['inventory'].iloc[0]

dfassets_tbl=pd.DataFrame({
    "Cash":[CASH],
    "Inventory":[INVENTORY],
    "Receivables":[RECEIVABLES],
    "Assets":[ASSETS],
    "Liabilities":[LIABILITIES]
})

dfdebt_tbl=pd.DataFrame({
    "Short Term Debt":[SHORTDEBT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ],
    "Long Term Debt":[LONGDEBT]
})

req13 = requests.get(f'https://financialmodelingprep.com/api/v4/insider-trading?symbol={symbol}?&page=0&apikey={creds.api_key}')
data13 = req13.json()
insidertrading = json_normalize(data13)
dfinside = pd.DataFrame(insidertrading)
#print(dfinside)




st.sidebar.text("PROFILE")
st.sidebar.dataframe(dfprofile_tbl1, use_container_width=True)
st.sidebar.dataframe(dfprofile_tbl2, use_container_width=True)
st.sidebar.text("Use Sliders For Additional Values")
st.sidebar.text("QUOTE")
st.sidebar.dataframe(quote_tbl, use_container_width=True)
st.sidebar.text("VALUE INDICATORS")
st.sidebar.dataframe(value_tbl, use_container_width=True)
st.sidebar.text("BASICS")
st.sidebar.dataframe(basic_tbl, use_container_width=True)
st.sidebar.text("CASH")
st.sidebar.dataframe(cash_tbl, use_container_width=True)
st.sidebar.text("DIVIDENDS")
st.sidebar.dataframe(div_tbl, use_container_width=True)
st.sidebar.text("DEBT")
st.sidebar.dataframe(debt_tbl, use_container_width=True)



col1, col2 = st.columns([2, 3], gap="large")

with col1:
    st.subheader("PEG Ratio:")
    st.write(peg_tbl)
    st.subheader("Relative Strength Index: ")
    st.write(RSI)
    st.subheader("Book Value Per Share: ")
    st.write(BOOK)
    st.subheader("EPS: ")
    st.write(EPS)
    st.subheader("Revenue and Profitability")
    st.dataframe(dfrev_tbl)
    st.dataframe(dfprofit_tbl)
    st.subheader("Assets and Liabilities")
    st.dataframe(dfassets_tbl)
    st.write("Net Earnings: ", NetEarnings)
    st.subheader("Income Statement")
    st.dataframe(dfincome)
    
   
    

with col2:
    st.subheader("Valuation Metrics")
    st.write(f"Current Price: {current_price}")
    st.write(f"Discounted Cash Flow (DCF): {dcf_value}")
    st.write(f"Intrinsic Value: {intrinsic_value}")
    st.subheader("Growth Rates")
    st.write(dfgeps_tbl)
    st.write(dfgrev_tbl)
    st.write(dfginc_tbl)
    st.subheader("Costs and Expenses")
    st.write(dfcosts_tbl)
    st.subheader("Debt")
    st.write(dfdebt_tbl)
    st.subheader("Insider Transactions")
    st.write(dfinside)