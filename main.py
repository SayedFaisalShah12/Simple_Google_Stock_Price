# %%
import yfinance as yf
import streamlit as st
import pandas as pd

# %%
st.write("""
         Shown are the stock closing price and volume of Google!
""")

# %%
tickerSymbol = 'GOOGL'

# %%
tickerData = yf.Ticker(tickerSymbol)

# %%
tickerDf = tickerData.history(
    start='2025-01-25',
    end='2030-01-25'
)


# %%
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)



