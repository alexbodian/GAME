import dash
import dash_core_components as dcc
import dash_html_components as html
import gdax
import plotly
from dash.dependencies import Input, Output, Event
import gdax
import datetime
import pytz
import random
from timezonefinder import TimezoneFinder
import pytz
from pytz import timezone, utc
from pytz.exceptions import UnknownTimeZoneError
import pandas as pd
import plotly
import plotly.graph_objs as go
from collections import deque
from plotly.graph_objs import *
import json
mapbox_access_token = 'pk.eyJ1IjoiYWxleC1ib2RpYW4iLCJhIjoiY2pmaGVwZGRzNGQ4NDJ4bzFpeWNtM3N5YyJ9.kqDjoO1nF1YuiVynmcbcDw'
import numpy as np

df = pd.read_csv('laws.csv') 
law_codes = pd.read_excel('codebook.xlsx')

# print(law_codes['Brief Description of Provision'])
# codes = df[(df['code'] == 'code')]

# print(df[(df['code'] == 'CT') & (df['year'] == 2000)])

test = df[(df['code'] == 'CT') & (df['year'] == 1991)]

# print(code)

# print(test)
# skip 0, 1, 2, 136
# print(len(test))
notthis = [0,1,2,136]
count = 0

# print(codes['Variable Name'])
# print(law_codes.columns.values.tolist())

# 133
laws_list = []
for i in range(0,133):
    laws_list.append(law_codes.iloc[i,3])
   
# print(laws_list)

laws_headers = test.columns.values.tolist()


# laws_headers.remove('code')
# laws_headers.remove('state')
# laws_headers.remove('year')
# laws_headers.remove('lawtotal')
# print(laws_headers)
lawsInState = []


for i in range(0,137):
    if i not in notthis: 
        # print(test.iloc[0,i])
        if test.iloc[0,i] == 1:
            lawsInState.append(laws_headers[i])

# print(lawsInState)
# Category Code.3
sorted(lawsInState, key=str.lower)
lawsInStateDFList = []

for i in range(0, len(lawsInState)):
    test1 = law_codes[(law_codes['Category Code.3'] == lawsInState[i])]
    lawsInStateDFList.append(test1)

print(lawsInStateDFList)    
lawsInStateDF = pd.concat(lawsInStateDFList)

print(lawsInStateDF)
# for i in range(1, len(lawsInState)):
#     lawsInStateDF.concat(lawsInStateDFList[i]      )
        
    

