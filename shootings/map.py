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
mapbox_access_token = "pk.eyJ1IjoiamFja3AiLCJhIjoidGpzN0lXVSJ9.7YK6eRwUNFwd3ODZff6JvA"
import plotly
import pandas as pd
from plotly.graph_objs import *
plotly.tools.set_credentials_file(username='alex-bodian', api_key='kEQkmyYsbqOBY2UirpMq')
mapbox_access_token = 'pk.eyJ1IjoiYWxleC1ib2RpYW4iLCJhIjoiY2pmaGVwZGRzNGQ4NDJ4bzFpeWNtM3N5YyJ9.kqDjoO1nF1YuiVynmcbcDw'

# https://automating-gis-processes.github.io/2016/Lesson5-interactive-map-folium.html

29.392825	-95.141972



# google images integration
# https://stackoverflow.com/questions/40672983/can-i-use-mapbox-for-street-view-like-google-maps-street-view

# https://www.mapbox.com/api-documentation/?language=Python#maps


data = Data([
    Scattermapbox(


        lat=['29.392825'],
        lon=['-95.141972'],
        mode='markers',
        marker=dict(
            size = 14,


            ),

        text='file_list',
    ),

])

layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
        lat=29.392825,
        lon=-95.141972
        ),
        pitch=0,
        zoom=3
    ),
)

fig = dict(data=data, layout=layout)
plotly.plotly.iplot(fig, filename='Scripting_Project', auto_open =True) #true makes it so that auto opens a web browser
