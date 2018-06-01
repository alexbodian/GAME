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

app = dash.Dash()
# https://goo.gl/f75Ufn
# chrolopleth info

app.layout = html.Div(children=[



    html.Div(

        children=dcc.Graph(
            id='graph',
            figure={
                'data': [{
                    'lat': 30, 'lon': 30, 'type': 'choropleth', 'locationmode': 'USA-states',
                }],
                'layout': {
                    'geo': {
                        'scope': (
                            'usa'
                        )
                    },
                    'margin': {
                        'l': 0, 'r': 0, 'b': 0, 't': 0
                    },
                }
            }
        )
    )
])
    






#     html.Div(

#         children=dcc.Graph(
#             id='graph',
#             figure={
#                 'data': [{
#                     'lat': 30, 'lon': 30, 'type': 'choropleth', 'locationmode': 'USA-states',
#                 }],
#                 'layout': {
#                     'mapbox': {
#                         'accesstoken': (
#                             'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3M' +
#                             'DBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
#                         )
#                     },
#                     'margin': {
#                         'l': 0, 'r': 0, 'b': 0, 't': 0
#                     },
#                 }
#             }
#         )
#     )
# ])





		# dcc.Graph(
		# 	id = 'county-choropleth',
		# 	figure = dict(
		# 		data=dict(
		# 			lat = df_lat_lon['Latitude '],
		# 			lon = df_lat_lon['Longitude'],
		# 			text = df_lat_lon['Hover'],
		# 			type = 'scattermapbox'
		# 		),
		# 		layout = dict(
		# 			mapbox = dict(
		# 				layers = [],
		# 				accesstoken = mapbox_access_token,
		# 				style = 'light',
		# 				center=dict(
		# 					lat=38.72490,
		# 					lon=-95.61446,
		# 				),
		# 				pitch=0,
		# 				zoom=2.5
		# 			)
		# 		)
		# 	)
		# )



if __name__ == '__main__':
	app.run_server(debug=True)