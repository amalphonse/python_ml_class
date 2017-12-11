# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:20:45 2017

@author: Anju
"""

"""
This script uses pandas-datareader to get prices from google.com
"""

import pandas_datareader as pdr
import datetime


start_dt = datetime.datetime(2017,1,1)
end_dt = datetime.datetime(2027,12,31)

prices_df = pdr.DataReader('IBM','google',start_dt,end_dt)
print(prices_df.head())

prices_df.to_csv('prices_ibm.csv',float_format='%4.3f')

