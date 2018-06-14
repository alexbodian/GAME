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
import json
mapbox_access_token = "pk.eyJ1IjoiamFja3AiLCJhIjoidGpzN0lXVSJ9.7YK6eRwUNFwd3ODZff6JvA"

df = pd.read_csv('laws.csv')

# df = (df[df['year'] == 2000])
# # print(df_2000)
# for col in df.columns:
#     df[col] = df[col].astype(str)


# marks. marks is a dict where the keys represent the numerical values
#  and the values represent their labels.
# keys must be a string

year_options = []
range_dict = {}
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})
    range_dict[str(year)] = year

# year_dict =


scl = [[0.0, 'rgb(246,239,247)'],[0.2, 'rgb(208,209,230)'],[0.4, 'rgb(166,189,219)'],\
            [0.6, 'rgb(103,169,207)'],[0.8, 'rgb(28,144,153)'],[1.0, 'rgb(1,108,89)']]


# scl = [[0.0, 'rgb(255,255,224)'],[0.1, 'rgb(255,230,178)'],[0.2, 'rgb(255,203,145)'],[0.3, 'rgb(255,174,121)'],\
#  [0.4, 'rgb(254,144,106)'],[0.5, 'rgb(244,116,97)'],[0.6, 'rgb(231,87,88)'],\
#  [0.7, 'rgb(213,60,76)'],[0.8, 'rgb(192,34,59)'],[0.9, 'rgb(167,11,36)'],[1.0, 'rgb(139,0,0)']]




app = dash.Dash()
# https://goo.gl/f75Ufn
# chrolopleth info


app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    # dcc.Dropdown(id='year-picker', options=year_options,value=df['year'].min())

    dcc.Slider(
    id='year-picker',
    min = df['year'].min(),
    max = df['year'].max(),
    marks = range_dict,
    value = df['year'].min(),
    ),
    html.Div(html.Pre(id='hover-data', style = {'paddingTop': 35}),
    style={'width':'30%'}),



],style={'width':'80%','float':'left'})

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
                colorscale = scl,
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
            title = 'US Firearms Provisions by State for ' + str(selected_year),
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


@app.callback(Output('hover-data','children'),
                [Input('graph-with-slider', 'hoverData')] #hoverdata is in every graph
)
def callback_image(hoverData):
    return json.dumps(hoverData,indent=2)




if __name__ == '__main__':
	app.run_server(debug=True)
