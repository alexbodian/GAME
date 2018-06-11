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

df = pd.read_csv('laws.csv')

# df = (df[df['year'] == 2000])
# # print(df_2000)
# for col in df.columns:
#     df[col] = df[col].astype(str)

year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})



scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]







app = dash.Dash()
# https://goo.gl/f75Ufn
# chrolopleth info


app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Dropdown(id='year-picker', options=year_options,value=df['year'].min())

])

@app.callback(Output('graph-with-slider', 'figure'),
             [Input('year-picker','value')])
def update_figure(selected_year):
    
    # filtered_df becomes a subset of the main df and contains all the
    # data but only for the selected year

    
    filtered_df = df[df['year'] == selected_year]

    # treat the filtered_df like the df in the original version since
    # it has the relevant data for the year and should produce the correct
    # graph
    #  df -> filtered_df

    for col in filtered_df.columns:
        filtered_df[col] = filtered_df[col].astype(str)

    filtered_df['text'] = filtered_df['state'] + '<br>' +\
    'age18longgunpossess ' + filtered_df['age18longgunpossess']+ ' age18longgunsale '+ filtered_df['age18longgunsale'] 

    
    return {
        'data' : [
            go.Choropleth(
                # colorscale = scl,
                autocolorscale = False,
                locations =  filtered_df['code'],
                z =  filtered_df['lawtotal'].astype(float),
                locationmode='USA-states',
                text= filtered_df['text'],
                marker=dict(
                    line=dict(
                        color='rgb(255,255,255)',
                        width=2
                    )),
                # colorbar=dict(
                #     title="Millions USD")
            )],
        'layout': go.Layout(
            title = 'US Firearms Provisions by State<br>(Hover for breakdown)',
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







if __name__ == '__main__':
	app.run_server(debug=True)