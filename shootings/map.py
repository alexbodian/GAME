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



df = pd.read_csv('https://docs.google.com/spreadsheets/d/1b9o6uDO18sLxBqPwl_Gh9bnhW-ev_dABH83M5Vb5L8o/export?format=csv&gid=0')


# print(df['case'])

# list of lists
# 0            1         2          3        4     5
# case name , location, date, total victims, lat, lon

desc = []
lat = []
lon = []


for i in range(0, df.shape[0]):


    text = df.loc[i, 'case'] + '\n'  \
    + df.loc[i, 'location'] + '\n'  \
    + df.loc[i, 'date'] + '\n'  \
    + 'Casualties: ' + str(df.loc[i, 'total_victims'])

    desc.append(text)

    lat.append(df.loc[i, 'latitude'])
    lon.append(df.loc[i, 'longitude'])


app = dash.Dash()

app.layout = html.Div([dcc.Graph(id='shooting_locations',
                    figure = {'data': [
                        go.Scattermapbox(
                            lat=lat,
                            lon=lon,
                            mode='markers',
                            marker = {
                                'size' :14,
                                },
                            text=desc,
                        )],
                    'layout': go.Layout(
                            title = 'US Mass Shooting Locations', 
                            width = 1200,
                            height = 800,
                            autosize=True,
                            hovermode='closest',
                            mapbox=dict(
                                accesstoken=mapbox_access_token,
                                bearing=0,
                                center=dict(
                                    lat=39.5,
                                    lon=-98.35
                                            ),
                                pitch=0,
                                zoom=2
                                ),
                                )
                    
                    
                    
                    }




)])

if __name__ == '__main__':
    app.run_server()





# data = Data([
#     Scattermapbox(


#         lat=lat,
#         lon=lon,
#         mode='markers',
#         marker=dict(
#             size = 14,


#             ),

#         text= desc,
#     ),

# ])

# layout = Layout(
#     autosize=True,
#     hovermode='closest',
#     mapbox=dict(
#         accesstoken=mapbox_access_token,
#         bearing=0,
#         center=dict(
#         lat=39.5,
#         lon=-98.35
#         ),
#         pitch=0,
#         zoom=3
#     ),
# )

# fig = dict(data=data, layout=layout)
# plotly.plotly.iplot(fig, filename='Scripting_Project', auto_open =True) #true makes it so that auto opens a web browser
