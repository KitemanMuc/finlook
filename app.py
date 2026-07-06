import streamlit as st
import yfinance as yf

ticker = yf.Ticker("GOOG")

st.title("FinLook")
hist = ticker.history(period="6mo")

st.write("Hello World")

print(hist.head())