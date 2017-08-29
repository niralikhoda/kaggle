# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 06:00:53 2017

@author: niralikhoda
"""

import pandas as pd
import numpy as np
import os
import datetime as dt
import matplotlib.pyplot as plt


cwd = os.getcwd()
os.chdir("C:\\Users\\niralikhoda\\kaggle\\cryptocurrencypricehistory")

df = pd.read_excel(open('bitcoin_cash_price.xlsx','rb'), sheetname='bitcoin_cash_price')

#############
df.head()

#df.plot(c='k', title='Example time series')


x = pd.to_datetime(df['Date'])
y,z = df['Open'],df['Close']


plt.plot(x, y)
plt.plot(x, z)
plt.show()