import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple stock price app
""")

tesla = yf.Ticker('TSLA')

tickerDf = tesla.history(period='1d', start='2010-01-01', end='2020-12-31')

st.write("""
### Tesla's closing prices from 1st Jan 2010 to 31st Dec 2020
""")
st.line_chart(tickerDf.Close)


st.write("""
### Tesla's volume prices from 1st Jan 2010 to 31st Dec 2020
""")
st.line_chart(tickerDf.Volume)


st.write("""
### Tesla's major holders
""")
tesla.major_holders


st.write("""
### Tesla's quarterly balance sheet
""")
tesla.quarterly_balance_sheet


st.write("""
### Some extra information
""")
tesla.info
