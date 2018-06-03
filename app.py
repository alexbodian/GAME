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

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

df['text'] = df['state'] + '<br>' +\
    'Beef '+df['beef']+' Dairy '+df['dairy']+'<br>'+\
    'Fruits '+df['total fruits']+' Veggies ' + df['total veggies']+'<br>'+\
    'Wheat '+df['wheat']+' Corn '+df['corn']

app = dash.Dash()
# https://goo.gl/f75Ufn
# chrolopleth info


app.layout = html.Div([
    dcc.Graph(
        id = 'graph',
        figure = {
            'data' : [
                go.Choropleth(
                    # colorscale = scl,
                    autocolorscale = False,
                    locations = df['code'],
                    z = df['total exports'].astype(float),
                    locationmode='USA-states',
                    text=df['text'],
                    marker=dict(
                        line=dict(
                            color='rgb(255,255,255)',
                            width=2
                        )),
                    # colorbar=dict(
                    #     title="Millions USD")
                )],
            'layout': go.Layout(
                title = '2011 US Agriculture Exports by State<br>(Hover for breakdown)',
                width = 800,
                height = 800,
                geo = dict(
                    scope = 'usa',
                    projection = dict (type= 'albers usa'),
                    showlakes = True,
                    lakecolor = 'rgb(255,255,255)',
                )



            )




        }
    )
])



















# app.layout = html.Div(children=[
#
#
#
#     html.Div(
#
#         children=dcc.Graph(
#             id='graph',
#             figure={
#                 'data': [{
#                     'lat': 30, 'lon': 30, 'type': 'choropleth', 'locationmode': 'USA-states',
#                 }],
#                 'layout': {
#                     'geo': {
#                         'scope': (
#                             'usa'
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

# import plotly.plotly as py
# import pandas as pd
#
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
#
# for col in df.columns:
#     df[col] = df[col].astype(str)
#
# scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], \
#        [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]
#
# df['text'] = df['state'] + '<br>' + \
#              'Beef ' + df['beef'] + ' Dairy ' + df['dairy'] + '<br>' + \
#              'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
#              'Wheat ' + df['wheat'] + ' Corn ' + df['corn']
#
# data = [dict(
#     type='choropleth',
#     colorscale=scl,
#     autocolorscale=False,
#     locations=df['code'],
#     z=df['total exports'].astype(float),
#     locationmode='USA-states',
#     text=df['text'],
#     marker=dict(
#         line=dict(
#             color='rgb(255,255,255)',
#             width=2
#         )),
#     colorbar=dict(
#         title="Millions USD")
# )]
#
# layout = dict(
#     title='2011 US Agriculture Exports by State<br>(Hover for breakdown)',
#     geo=dict(
#         scope='usa',
#         projection=dict(type='albers usa'),
#         showlakes=True,
#         lakecolor='rgb(255, 255, 255)'),
# )
#
# fig = dict(data=data, layout=layout)
# py.iplot(fig, filename='d3-cloropleth-map')



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