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

state_to_code = {
    # # Other
    # 'District of Columbia': 'DC',
    
    # States
    'Alabama': 'AL',
    'Montana': 'MT',
    'Alaska': 'AK',
    'Nebraska': 'NE',
    'Arizona': 'AZ',
    'Nevada': 'NV',
    'Arkansas': 'AR',
    'New Hampshire': 'NH',
    'California': 'CA',
    'New Jersey': 'NJ',
    'Colorado': 'CO',
    'New Mexico': 'NM',
    'Connecticut': 'CT',
    'New York': 'NY',
    'Delaware': 'DE',
    'North Carolina': 'NC',
    'Florida': 'FL',
    'North Dakota': 'ND',
    'Georgia': 'GA',
    'Ohio': 'OH',
    'Hawaii': 'HI',
    'Oklahoma': 'OK',
    'Idaho': 'ID',
    'Oregon': 'OR',
    'Illinois': 'IL',
    'Pennsylvania': 'PA',
    'Indiana': 'IN',
    'Rhode Island': 'RI',
    'Iowa': 'IA',
    'South Carolina': 'SC',
    'Kansas': 'KS',
    'South Dakota': 'SD',
    'Kentucky': 'KY',
    'Tennessee': 'TN',
    'Louisiana': 'LA',
    'Texas': 'TX',
    'Maine': 'ME',
    'Utah': 'UT',
    'Maryland': 'MD',
    'Vermont': 'VT',
    'Massachusetts': 'MA',
    'Virginia': 'VA',
    'Michigan': 'MI',
    'Washington': 'WA',
    'Minnesota': 'MN',
    'West Virginia': 'WV',
    'Mississippi': 'MS',
    'Wisconsin': 'WI',
    'Missouri': 'MO',
    'Wyoming': 'WY',
}

monthes = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August','September','October','November','December']


db = pd.read_csv('nics-firearm-background-checks.csv')

# year_month = []

# month_list = ['-01','-02', '-03', '-04', '-05', '-06', '-07', \
#                '-08','-09','-10','-11','-12' ]

# year = '2004'
# for i in month_list:
#     curr = year + i
#     year_month.append(curr)
#     # print(curr)

# dx = df[(df.month.isin(year_month)) & (df.state == 'Connecticut')]

# # reverse df
# dx = dx.iloc[::-1]





code_to_state = {v: k for k, v in state_to_code.items()}

df = pd.read_csv('laws.csv')

# df = (df[df['year'] == 2000])
# # print(df_2000)
# for col in df.columns:
#     df[col] = df[col].astype(str)


# marks. marks is a dict where the keys represent the numerical values
#  and the values represent their labels.
# keys must be a string

curr_year = ''
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

    html.Div([    
    dcc.Graph(id='graph-with-slider'),
    # dcc.Dropdown(id='year-picker', options=year_options,value=df['year'].min())
    dcc.Slider(
    id='year-picker',
    min = df['year'].min(),
    max = df['year'].max(),
    marks = range_dict,
    value = df['year'].min(),
    ),],style={'width':'80%', 'height': '70%','float':'center', 'paddingLeft': 35, 'display': 'inline-block', 'paddingBottom':35}),


    html.Div([dcc.Graph(id='background-scatter', 
                    figure = {'data': [
                        go.Scatter(
                            x=monthes,
                            y=[0,0,0,0,0,0,0,0,0,0,0,0],
                            mode='lines+markers',
                            marker = {
                                'size' :12,
                                'color': 'rgb(51,204,153)',
                                'line':{'width':1},
                            }
                        )],
                    'layout': go.Layout(title= 'Background checks',
                                            yaxis = {'range': [0,db['totals'].min()]},
                                            xaxis= {'title': 'Month'})}
                    ),
                    
],style={'width': '80%', 'height':'80%', 'display':'inline-block'}),


    html.Div(html.Pre(id='hover-data', style = {'paddingTop': 35}),
    style={'width':'30%'}),
            ])


# @app.callback(Output('background-scatter', 'figure'),
#              [Input('graph-with-slider','value')])

@app.callback(Output('background-scatter','figure'),
                [Input('graph-with-slider', 'hoverData')])
def callback_graph(hoverData):
    #     state = hoverData['points'][0]['location']
    # year = hoverData['points'][0]['customdata']
    # # return year
    # return json.dumps(hoverData,indent=2)
    # # return code_to_state[state] + ' ' + curr_year
    # # return curr_year
    month_list = ['-01','-02', '-03', '-04', '-05', '-06', '-07','-08','-09','-10','-11','-12' ]

    state = hoverData['points'][0]['location']
    state = code_to_state[state]
    year = hoverData['points'][0]['customdata']
    title = str(year) + ' ' + state + ' background checks'

    year_month = []

    for i in month_list:
        curr = str(year) + i
        year_month.append(curr)
    
    dx = db[(db.month.isin(year_month)) & (db.state == state)]

# reverse df
    dx = dx.iloc[::-1]



    if year < 1999:
        temp = [0,0,0,0,0,0,0,0,0,0,0,0]
        figure = {'data': [
                            go.Scatter(
                                x=monthes,
                                y=temp,
                                mode='lines+markers',
                                marker = {
                                    'size' :12,
                                    'color': 'rgb(51,204,153)',
                                    'line':{'width':1},
                                }
                            )],
                        'layout': go.Layout(title= title,
                                            # yaxis = {'range': [0,(db['totals'].min())]},
                                            xaxis= {'title': 'Month'})}

    else:
       figure = {'data': [
                        go.Scatter(
                            x=monthes,
                            y=dx['totals'],
                            mode='lines+markers',
                            marker = {
                                'size' :12,
                                'color': 'rgb(51,204,153)',
                                'line':{'width':1},
                            }
                        )],
                    'layout': go.Layout(title= title,
                                            # yaxis = {'range': [0,(db['totals'].min())]},
                                            xaxis= {'title': 'Month'})}

    
    return figure









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

    year_list = []
    for col in filtered_df.columns:
        filtered_df[col] = filtered_df[col].astype(str)
        year_list.append(selected_year)

    filtered_df['text'] = filtered_df['state'] + '<br>' +\
    'age18longgunpossess ' + filtered_df['age18longgunpossess']+ ' age18longgunsale '+ filtered_df['age18longgunsale']
    

    return {
        'data' : [
            go.Choropleth(
                colorscale = scl,
                autocolorscale = False,
                customdata = year_list,
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


# @app.callback(Output('hover-data','children'),
#                 [Input('graph-with-slider', 'hoverData')] #hoverdata is in every graph
# )
# def callback_image(hoverData):
#     state = hoverData['points'][0]['location']
#     year = hoverData['points'][0]['customdata']
#     # return year
#     return json.dumps(hoverData,indent=2)
#     # return code_to_state[state] + ' ' + curr_year
#     # return curr_year




if __name__ == '__main__':
	app.run_server(debug=True)
