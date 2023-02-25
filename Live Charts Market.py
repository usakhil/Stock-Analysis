#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install yfinance


# In[5]:


import yfinance as yf
import plotly.graph_objs as go


# In[4]:


pip install pandas --upgrade


# In[3]:


import numpy
print(numpy.version.version)


# In[6]:


stock_name = "TSLA"

T = '1d'

delta_t = '1m'

data = yf.download(tickers = stock_name, period = T, interval = delta_t)

data


# In[7]:


fig = go.Figure()

fig.add_trace(
    go.Candlestick(
        x = data.index,
        open = data['Open'],
        high = data['High'],
        low = data['Low'],
        close = data['Close'],
        name = 'Market Prices'
    )
)


# In[ ]:


stock_input = str(input("Pick Your Ticker: "))

Period_input = input("Period: ")

Time_interval_input = input("Time: ")

stock_name = '{}'.format(stock_input.upper())
                          
T = '{}'.format(Period_input)

delta_t = '{}'.format(Time_interval_input)

data = yf.download(tickers = stock_name, period = T, interval = delta_t)

data.tail()

fig = go.Figure()

fig.add_trace(
    go.Candlestick(
        x = data.index,
        open = data['Open'],
        high = data['High'],
        low = data['Low'],
        close = data['Close'],
        name = 'Market Prices'
    ))

fig.update_layout(
title = "Live Market Data ",
yaxis_title = 'Stock Price (per share)')
    
fig.update_xaxes(
rangeslider_visible = True,
rangeselector = dict(
    buttons = list([
    dict(count = 5, label="5m", step="minute", stepmode ="backward"),
    dict(count = 60,label = 'HTD', step = "minute", stepmode="backward")        
])))

