import yfinance as yf
import pandas as pd
import numpy as np

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]

data = yf.download(tickers, start="2013-01-01", end="2024-01-01")["Adj Close"]
data = data.dropna(how="all").ffill().dropna()

returns = data.pct_change().dropna()

data.to_csv("clean_prices.csv")
returns.to_csv("clean_returns.csv")

data.head(), returns.head()

