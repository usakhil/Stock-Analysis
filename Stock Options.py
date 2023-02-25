#!/usr/bin/env python
# coding: utf-8

# In[34]:


pip install yfinance


# In[35]:


pip install numexpr


# In[36]:


import numpy as np

from datetime import datetime, timedelta
import yfinance as yf

import matplotlib.pyplot as plt


# In[49]:


stock_name = 'SPY'

end_date = datetime.today()
n_years = 1
start_date = end_date - timedelta(days = n_years*365)

stock_data = yf.download(tickers =stock_name, start = start_date, end = end_date)
stock_prices = stock_data['Adj Close']

log_returns = np.log(stock_prices/stock_prices.shift(1)).dropna()

trading_days_year = 252
trading_days_month = 21
volatility = log_returns.rolling(window = trading_days_month).std() * np.sqrt(trading_days_year)

volatility.tail()


# In[72]:


stock_input = input("Pick a stock: ")


fig, ax  = plt.subplots()
ax.plot(stock_prices, color = 'red')
ax.set_xlabel("Date", fontsize = 14)
ax.set_ylabel("Stock price", color = "red", fontsize = 14)

ax2 = ax.twinx()
ax2.plot(volatility, color = 'blue')
ax2.set_ylabel("Volatility", color = 'blue', fontsize = 14)

plt.show()
stock_name = '{}'.format(stock_input.upper())

end_date = datetime.today()
n_years = 1
start_date = end_date - timedelta(days = n_years*365)

stock_data = yf.download(tickers =stock_name, start = start_date, end = end_date)
stock_prices = stock_data['Adj Close']

log_returns = np.log(stock_prices/stock_prices.shift(1)).dropna()

trading_days_year = 252
trading_days_month = 21
volatility = log_returns.rolling(window = trading_days_month).std() * np.sqrt(trading_days_year)

volatility.tail()


# In[ ]:


fig, ax  = plt.subplots()
ax.plot(stock_prices, color = 'red')
ax.set_xlabel("Date", fontsize = 14)
ax.set_ylabel("Stock price", color = "red", fontsize = 14)

ax2 = ax.twinx()
ax2.plot(volatility, color = 'blue')
ax2.set_ylabel("Volatility", color = 'blue', fontsize = 14)

plt.show()


# In[57]:


pip install py_vollib


# In[61]:


# B&S call pric
from py_vollib.black_scholes import black_scholes as bs

