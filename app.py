import streamlit as st
import yfinance as yf

st.set_page_config(page_title="FinLook", layout="wide")

st.title("FinLook")
st.write("Investment Monitoring Dashboard")

symbol = st.text_input("Ticker", "GOOG")

ticker = yf.Ticker(symbol)
hist = ticker.history(period="6mo")

st.subheader(f"Historische Daten: {symbol}")
st.dataframe(hist.tail(20))

st.subheader("Close Price Chart")
st.line_chart(hist["Close"])