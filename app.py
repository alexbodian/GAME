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

def generate_table(dataframe):
    max_rows = 40

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

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

df_shooting = pd.read_csv('https://docs.google.com/spreadsheets/d/1b9o6uDO18sLxBqPwl_Gh9bnhW-ev_dABH83M5Vb5L8o/export?format=csv&gid=0')
dfKaggle = pd.read_csv('Mass Shootings Dataset Ver 2.csv',encoding='latin1')

# print(df_shooting['case'])

# list of lists
# 0            1         2          3        4     5
# case name , location, date, total victims, lat, lon

desc = []
lat = []
lon = []
years = []

loc =[]
date=[]
totalVic=[]

locKaggle=[]
dateKaggle=[]
totalVicKaggle=[]
latKaggle=[]
lonKaggle=[]

for i in range(0, df_shooting.shape[0]):
    loc.append(df_shooting.loc[i, 'location'] + '\n')
    date.append(df_shooting.loc[i, 'date'] + '\n')
    totalVic.append(str(df_shooting.loc[i, 'total_victims']))

    text = df_shooting.loc[i, 'case'] + '\n'  \
    + loc[i]  \
    + date[i]  \
    + 'Casualties: ' + totalVic[i]
    desc.append(text)

    lat.append(df_shooting.loc[i, 'latitude'])
    lon.append(df_shooting.loc[i, 'longitude'])
    years.append(df_shooting.loc[i,'year'])

for i in range(0, dfKaggle.shape[0]):
    locKaggle.append("" if dfKaggle.loc[i, 'Location'] is np.nan else dfKaggle.loc[i, 'Location']  + '\n')
    dateKaggle.append(dfKaggle.loc[i, 'Date'] + '\n')
    totalVicKaggle.append(str(dfKaggle.loc[i, 'Total victims']))

for i in range(0,dfKaggle.shape[0]):
    flagDuplicate=False
    for j in range(0,df_shooting.shape[0]):
        if(flagDuplicate==False):
            if(date[j]==dateKaggle[i]):
                if(loc[j]==locKaggle[i]):
                    #if(totalVic[j]==totalVicKaggle[i]):
                        flagDuplicate=True
    if(flagDuplicate==False):
        Text = dfKaggle.loc[i, 'Title'] + '\n' \
        + locKaggle[i] \
        + dateKaggle[i] \
        + 'Casualties: ' + totalVicKaggle[i]
        desc.append(Text)
        lat.append(dfKaggle.loc[i, 'Latitude'])
        lon.append(dfKaggle.loc[i, 'Longitude'])
        #years.append(dfKaggle.loc[i,'year']) no such column so have to substring
        TempDateKaggle=dfKaggle.loc[i, 'Date']
        TempYearKaggle=TempDateKaggle[(len(TempDateKaggle)-4):]
        TempNum = int(TempYearKaggle)
        years.append(TempNum)

# print(year)
uniq_years = df_shooting['year'].unique()
uniq_years = uniq_years[::-1]
# print(type(uniq_years))
# uniq_years = uniq_years.iloc[::-1]
year_dict = {}
for i in uniq_years:
    year_dict[str(i)] = i





code_to_state = {v: k for k, v in state_to_code.items()}


df = pd.read_csv('laws.csv')
law_codes = pd.read_excel('codebook.xlsx')

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

test = df[(df['code'] == 'CT') & (df['year'] == 1991)]

notthis = [0,1,2,136]
count = 0
laws_list = []
for i in range(0,133):
    laws_list.append(law_codes.iloc[i,3])
laws_headers = test.columns.values.tolist()

lawsInState = []

for i in range(0,137):
    if i not in notthis: 
        if test.iloc[0,i] == 1:
            lawsInState.append(laws_headers[i])
sorted(lawsInState, key=str.lower)
lawsInStateDFList = []

for i in range(0, len(lawsInState)):
    test1 = law_codes[(law_codes['Category Code.3'] == lawsInState[i])]
    lawsInStateDFList.append(test1)


lawsInStateDF = pd.concat(lawsInStateDFList)




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
    ),],style={'width':'40%', 'height': '70%','float':'center', 'paddingLeft': 15, 'display': 'block', 'paddingBottom':35}),


#     html.Div([dcc.Graph(id='background-scatter',
#                     figure = {'data': [
#                         go.Scatter(
#                             x=monthes,
#                             y=[0,0,0,0,0,0,0,0,0,0,0,0],
#                             mode='lines+markers',
#                             marker = {
#                                 'size' :12,
#                                 'color': 'rgb(51,204,153)',
#                                 'line':{'width':1},
#                             }
#                         )],
#                     'layout': go.Layout(title= 'Background checks',
#                                             yaxis = {'range': [0,600000]},
#                                             xaxis= {'title': 'Month'})}
#                     ),

# ],style={'width': '40%', 'height':'90%', 'display':'inline-block'}),

 html.Div(id= 'provisions',children=[
    html.H4(children='Laws Connecticut 1991'),
    generate_table(lawsInStateDF)
],style={'height': '600px', 'width':'600px', 'display':'block', 'overflow-x': 'auto', 'overflow-y': 'scroll', 'border-style': 'solid', 'border-width': '1px'}),



    html.Div([dcc.Graph(id='background-scatter-lasso',
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
                                            yaxis = {'range': [0,600000]},
                                            xaxis= {'title': 'Month'})}
                    ),

],style={'width': '80%', 'height':'90%', 'display':'inline-block', 'paddingTop': '35'}),

    html.Div([

    dcc.Graph(id='shooting_locations'),

    dcc.RangeSlider(
        id='shooting_range',
        min=1982,
        max=2018,
        step=None,
        marks=year_dict,
        value=[1982,2018]
    )

    ],style={'width':'80%', 'paddingLeft': 35}),


    html.Div(html.Pre(id='hover-data', style = {'paddingTop': 35}),
    style={'width':'30%'}),
            ])


# @app.callback(Output('background-scatter', 'figure'),
#              [Input('graph-with-slider','value')])

# @app.callback(Output('background-scatter','figure'),
#                 [Input('graph-with-slider', 'hoverData')])
# def callback_graph(hoverData):
#     #     state = hoverData['points'][0]['location']
#     # year = hoverData['points'][0]['customdata']
#     # # return year
#     # return json.dumps(hoverData,indent=2)
#     # # return code_to_state[state] + ' ' + curr_year
#     # # return curr_year
#     month_list = ['-01','-02', '-03', '-04', '-05', '-06', '-07','-08','-09','-10','-11','-12' ]

#     state = hoverData['points'][0]['location']
#     state = code_to_state[state]
#     year = hoverData['points'][0]['customdata']
#     title = str(year) + ' ' + state + ' background checks'

#     year_month = []

#     for i in month_list:
#         curr = str(year) + i
#         year_month.append(curr)

#     dx = db[(db.month.isin(year_month)) & (db.state == state)]

# # reverse df
#     dx = dx.iloc[::-1]



#     if year < 1999:
#         temp = [0,0,0,0,0,0,0,0,0,0,0,0]
#         figure = {'data': [
#                             go.Scatter(
#                                 x=monthes,
#                                 y=temp,
#                                 mode='lines+markers',
#                                 marker = {
#                                     'size' :12,
#                                     'color': 'rgb(51,204,153)',
#                                     'line':{'width':1},
#                                 }
#                             )],
#                         'layout': go.Layout(title= title,
#                                             # yaxis = {'range': [0,(db['totals'].min())]},
#                                             xaxis= {'title': 'Month'},
#                                             yaxis = {'range': [0,600000]}
#                                             )}

#     else:
#        figure = {'data': [
#                         go.Scatter(
#                             x=monthes,
#                             y=dx['totals'],
#                             mode='lines+markers',
#                             marker = {
#                                 'size' :12,
#                                 'color': 'rgb(51,204,153)',
#                                 'line':{'width':1},
#                             }
#                         )],
#                     'layout': go.Layout(title= title,
#                                             # yaxis = {'range': [0,(db['totals'].min())]},
#                                             xaxis= {'title': 'Month'},
#                                             yaxis = {'range': [0,600000]}
#                                             )}


#     return figure





# @app.callback(Output('provisions','figure'),
#                 [Input('graph-with-slider', 'hoverData')])
# def callback_graph(hoverData):
#     #     state = hoverData['points'][0]['location']
#     # year = hoverData['points'][0]['customdata']
#     # # return year
#     # return json.dumps(hoverData,indent=2)
#     # # return code_to_state[state] + ' ' + curr_year
#     # # return curr_year
    




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

@app.callback(Output('provisions', 'children'),
                [Input('graph-with-slider','hoverData')])
def find_density(hoverData):
    
    code = hoverData['points'][0]['location']
    year = hoverData['points'][0]['customdata']
    



    test = df[(df['code'] == code) & (df['year'] == year)]

    notthis = [0,1,2,136]
    count = 0
    laws_list = []
    for i in range(0,133):
        laws_list.append(law_codes.iloc[i,3])
    laws_headers = test.columns.values.tolist()

    lawsInState = []

    for i in range(0,137):
        if i not in notthis: 
            if test.iloc[0,i] == 1:
                lawsInState.append(laws_headers[i])
    sorted(lawsInState, key=str.lower)
    lawsInStateDFList = []

    for i in range(0, len(lawsInState)):
        test1 = law_codes[(law_codes['Category Code.3'] == lawsInState[i])]
        lawsInStateDFList.append(test1)


    lawsInStateDF = pd.concat(lawsInStateDFList)

    return generate_table(lawsInStateDF)







    # calc density
    # pts = len(selectedData['points'])
    # rng_or_lp = selectedData
    # numOfStates = len(selectedData['points'])
    # print(selectedData['points'][0]['customdata'])


    # for i in range(0,numOfStates):
    #     print(code_to_state[selectedData['points'][i]['location']])

    # # print(len(rng_or_lp['points'])    )

    # return json.dumps(selectedData,indent=2)
    # # print( selectedData['points'][0]['location'])
    # # return selectedData['points'][0]['location']


@app.callback(Output('background-scatter-lasso', 'figure'),
                [Input('graph-with-slider','selectedData')])
def backgroundScatterLasso(selectedData):
    # calc density
    # pts = len(selectedData['points'])
    # rng_or_lp = selectedData


    numOfStates = len(selectedData['points'])
    year = selectedData['points'][0]['customdata']

    traces = []

    month_list = ['-01','-02', '-03', '-04', '-05', '-06', '-07','-08','-09','-10','-11','-12' ]
    year_month = []

    for i in month_list:
        curr = str(year) + i
        year_month.append(curr)




    if year < 1999:
        for i in range(0,numOfStates):
            temp = [0,0,0,0,0,0,0,0,0,0,0,0]
            traces.append(go.Scatter(
            x=monthes,
            y=temp,
            text=selectedData['points'][i]['text'],
            mode='lines+markers',
            opacity=0.7,
            marker={'size': 15},
            name=code_to_state[selectedData['points'][i]['location']]
        ))


                # go.Scatter(
                #             x=monthes,
                #             y=temp,
                #             mode='lines+markers',
                #             marker = {
                #                 'size' :12,
                #                 'color': 'rgb(51,204,153)',
                #                 'line':{'width':1},
                #             }
                #         )],
                #     'layout': go.Layout(title= title,
                #                         # yaxis = {'range': [0,(db['totals'].min())]},
                #                         xaxis= {'title': 'Month'},
                #                         yaxis = {'range': [0,600000]}
                #                         )}


    else:
        for i in range(0,numOfStates):
            dx = db[(db.month.isin(year_month)) & (db.state == code_to_state[selectedData['points'][i]['location']])]
            dx = dx.iloc[::-1]


            traces.append(go.Scatter(
            x=monthes,
            y=dx['totals'],
            text=selectedData['points'][i]['text'],
            mode='lines+markers',
            opacity=0.7,
            marker={'size': 15},
            name=code_to_state[selectedData['points'][i]['location']]
            ))



    return {
        'data': traces,
        'layout': go.Layout(
            title= str(year) + ' background checks',
            # yaxis = {'range': [0,(db['totals'].min())]},
            xaxis= {'title': 'Month'},
            yaxis = {'range': [0,600000]},
            hovermode='closet'

            )
    }

@app.callback(Output('shooting_locations', 'figure'),
             [Input('shooting_range','value')])
def update_locations(selected_years):
    # selected_years is a list


    # desc = []
    # lat = []
    # lon = []
    # year = []

    desc_temp = []
    lat_temp = []
    lon_temp = []
    year_temp = []

    count = 0



    for i in years:

        if (i >= selected_years[0]) and (i <= selected_years[1]):
            desc_temp.append(desc[count])
            lat_temp.append(lat[count])
            lon_temp.append(lon[count])
            year_temp.append(years[count])
        count += 1


    return {
        'data': [
            go.Scattermapbox(
                lat=lat_temp,
                lon=lon_temp,
                mode='markers',
                marker = {
                    'size' :14,
                    },
                text=desc_temp,
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




if __name__ == '__main__':
	app.run_server(debug=True)
