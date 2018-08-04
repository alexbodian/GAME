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
import os
from flask_caching import Cache





# function that generates the table that
# is used for the collapsable div 
# for displaying state laws
def generate_table(dataframe,title):
    max_rows = 40

    return html.Table(
        # Header
        [html.Tr(html.H5(title))] +

        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
            )


state_to_code = {
    # States
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
code_to_state = {v: k for k, v in state_to_code.items()}
StateCodes = list(code_to_state.keys())

monthes = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August','September','October','November','December']

db = pd.read_csv('nics-firearm-background-checks.csv')
df_shooting = pd.read_csv('https://docs.google.com/spreadsheets/d/1b9o6uDO18sLxBqPwl_Gh9bnhW-ev_dABH83M5Vb5L8o/export?format=csv&gid=0')
dfKaggle = pd.read_csv('Mass Shootings Dataset Ver 2.csv',encoding='latin1')



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
    loc.append(df_shooting.loc[i, 'location'])
    ddmmyyyy=df_shooting.loc[i, 'date'].split("/")
    tempdate=""
    if (len(ddmmyyyy[2])<3):
        ddmmyyyy[2]="20"+ddmmyyyy[2]
    for j in range(0,len(ddmmyyyy)):
        tempdate=tempdate+ddmmyyyy[j]
        if (j<2):
            tempdate=tempdate+"/"
    date.append(tempdate)

    totalVic.append(str(df_shooting.loc[i, 'total_victims']))

    text = df_shooting.loc[i, 'case'] + '<br>'  \
    + loc[i] + ' ' \
    + date[i]  \
    + ' Casualties: ' + totalVic[i] + '<br>'
    desc.append(text)

    lat.append(df_shooting.loc[i, 'latitude'])
    lon.append(df_shooting.loc[i, 'longitude'])
    years.append(df_shooting.loc[i,'year'])

for i in range(0, dfKaggle.shape[0]):
    locKaggle.append("" if dfKaggle.loc[i, 'Location'] is np.nan else dfKaggle.loc[i, 'Location'])
    dateKaggle.append(dfKaggle.loc[i, 'Date'])
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
        Text = dfKaggle.loc[i, 'Title'] + '<br>' \
        + locKaggle[i] + ' ' \
        + dateKaggle[i] \
        + ' Casualties: ' + totalVicKaggle[i] + '<br>'
        desc.append(Text)
        lat.append(dfKaggle.loc[i, 'Latitude'])
        lon.append(dfKaggle.loc[i, 'Longitude'])
        #years.append(dfKaggle.loc[i,'year']) no such column so have to substring
        TempDateKaggle=dfKaggle.loc[i, 'Date']
        TempYearKaggle=TempDateKaggle[(len(TempDateKaggle)-4):]
        date.append(TempDateKaggle)
        totalVic.append(totalVicKaggle[i])
        TempNum = int(TempYearKaggle)
        years.append(TempNum)
        loc.append(locKaggle[i])

# print(year)
#uniq_years = years.unique()
setyears=set(years)

uniq_years = list(setyears)
uniq_years = uniq_years[::-1]
# print(type(uniq_years))
# uniq_years = uniq_years.iloc[::-1]
year_dict = {}
for i in uniq_years:
    year_dict[str(i)] = i


shooting_monthes = []









df = pd.read_csv('laws.csv')
temp_codes = pd.read_excel('codebook.xlsx')

law_codes = temp_codes.loc[:,'Category Code.1':'Category Code.4']




# marks. marks is a dict where the keys represent the numerical values
#  and the values represent their labels.
# keys must be a string

curr_year = ''
year_options = []
range_dict = {}
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})
    range_dict[str(year)] = year



# this is the colorscale that is used in the choropleths
scl = [[0.0, 'rgb(246,239,247)'],[0.2, 'rgb(208,209,230)'],[0.4, 'rgb(166,189,219)'],\
            [0.6, 'rgb(103,169,207)'],[0.8, 'rgb(28,144,153)'],[1.0, 'rgb(1,108,89)']]




test = df[(df['code'] == 'CT') & (df['year'] == 2017)]

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

# this renames the headers for the state laws table
lawsInStateDF = pd.concat(lawsInStateDFList)
lawsInStateDFCT = lawsInStateDF
lawsInStateDFCT = lawsInStateDFCT.rename(index=str, columns={"Category Code.1": "Category", "Category Code.2": "Type", "Category Code.3": "Abbrieviation", "Category Code.4": "Description" })




app = dash.Dash(__name__)

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
# Append an externally hosted JS bundle
my_js_url = 'https://unkpg.com/some-npm-package.js'
app.scripts.append_script({"external_url": my_js_url})
server = app.server
app.layout = html.Div([

    html.Div([

html.Div([
    # this is the collapsable table for displaying specific state laws
    html.Details([
        html.Summary('(Click here to see all the laws for a state)'),
         html.Div(id= 'provisions',children=[
            generate_table(lawsInStateDFCT, 'Connecticut Laws 2017')
        ],style={'height': '600px', 'width':'600px', 'display':'inlineblock', 'paddingLeft': 5, 'paddingRight': 5, 'paddingBottom': 1,'overflow-x': 'auto', 'overflow-y': 'scroll', 'border-style': 'solid', 'border-width': '1px', 'float':'left'})]),]),


        html.Div([
        # state laws choropleth
        dcc.Graph(id='graph-with-slider')],style={'width':'30%', 'height': '70%','float':'left','margin': 0, 'paddingLeft': 0, 'display': 'inlineblock', 'paddingBottom':1, 'overflow': 'hidden'}),
        html.Div([
        # total background checks per year choropleth by state
        dcc.Graph(id='background-check-choropleth')],style={'width':'30%', 'height': '70%','float':'left', 'paddingLeft': 0, 'display': 'inlineblock', 'paddingBottom':1, 'overflow': 'hidden'}),
        html.Div([
        # mass shootings choropleth
        dcc.Graph(id='shootings-state-choropleth')],style={'width':'40%', 'height': '70%','float':'left', 'paddingLeft': 0, 'display': 'inlineblock', 'paddingBottom':1, 'overflow': 'hidden'}),
    ],style={'width':'100%', 'height': '60%','float':'left', 'paddingLeft': 10, 'display': 'inlineblock', 'paddingBottom':5}),

    html.Div([
    # main year slider that affects the year for the chorpleths and scatter plots
    dcc.Slider(
    id='year-picker',
    min = df['year'].min(),
    max = df['year'].max(),
    marks = range_dict,
    value = df['year'].max(),
    ),],style={'width':'90%', 'height': '65%','float':'left', 'paddingLeft': 55, 'display': 'block', 'paddingBottom':10}),




    # background checks by month state scatter plot
    html.Div([dcc.Graph(id='background-scatter-lasso',animate='false',
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

],style={'width': '50%', 'height':'50%', 'display':'inline-block', 'paddingTop': '8'}),
    # total mass shootings by month scatter plot
    html.Div([dcc.Graph(id='mass-shooting-scatter',animate='false',
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
                    'layout': go.Layout(title= 'Mass Shootings',
                                            yaxis = {'range': [0,5000], 'title': 'Total Victims'},
                                            xaxis= {'title': 'Month'})}
                    ),

],style={'width': '50%', 'height':'50%', 'display':'inline-block', 'paddingTop': '8'}),



    html.Div([
    # mapbox element that displays coordinates for mass shootings 
    dcc.Graph(id='shooting_locations',style={'paddingBottom':0}),

    # rangeslider that affects the years for mass shootings that are displayed
    # on the map
    dcc.RangeSlider(
        id='shooting_range',
        min=1982,
        max=2018,
        step=None,
        marks=year_dict,
        value=[1982,2018]
    )

    ],style={'width':'80%', 'paddingLeft': 35, 'paddingBottom': 50}),

   
            ],style={'height':'70%'})





# shootings in each state choropleth
@app.callback(Output('shootings-state-choropleth', 'figure'),
             [Input('year-picker','value')])
def update_figure(selected_year):

    # filtered_df becomes a subset of the main df and contains all the
    # data but only for the selected year

    year = selected_year



    listOfStates = list(state_to_code.keys())
    listOfCodes = list(code_to_state.keys())

    listOfShootings = []
    numOfShootings = []

    # init the list with blank strings
    for i in range(0, 50):
        formattedText = listOfStates[i] + '<br>'
        listOfShootings.append(formattedText)
        numOfShootings.append(0)




    for i in range(0, len(years)):
        if years[i] == year:

            for j in range(0,50):
                if (listOfStates[j] in loc[i]) or (listOfCodes[j] in loc[i]):
                        listOfShootings[j] += desc[i] + '<br>'
                        numOfShootings[j] += 1





    trace = [

        go.Choropleth(
        colorscale = scl,
                autocolorscale = False,
                locations =  listOfCodes,
                z =  numOfShootings,
                text = listOfShootings,
                locationmode='USA-states',
                marker=dict(
                    line=dict(
                        color='rgb(255,255,255)',
                        width=2
                    )),
                # colorbar=dict(
                #     title="Total Mass Shootings")
                #

        )]




    return {
        'data': trace,
        'layout': go.Layout(
            title = 'US Mass Shootings ' + str(selected_year) + '<br>' + '(Total Mass Shootings)',
            width = 600,
            height = 600,
            geo = dict(
                scope = 'usa',
                projection = dict (type= 'albers usa'),
                showlakes = True,
                lakecolor = 'rgb(255,255,255)',
                    )
                    )
            }





# State background checks choropleth
@app.callback(Output('background-check-choropleth', 'figure'),
             [Input('year-picker','value')])
def update_figure(selected_year):

    # filtered_df becomes a subset of the main df and contains all the
    # data but only for the selected year



    # treat the filtered_df like the df in the original version since
    # it has the relevant data for the year and should produce the correct
    # graph
    #  df -> filtered_df=
    month_list = ['-01','-02', '-03', '-04', '-05', '-06', '-07','-08','-09','-10','-11','-12' ]
    year_month = []
    totalBackgroundChecks = []

    # appending the year to the month
    for i in month_list:
        curr = str(year) + i
        year_month.append(curr)

    # setting each index in the backgroundchecks list to 0
    for i in range(0,50):
        totalBackgroundChecks.append(0)


    if selected_year > 1998:
        for i  in range(0, len(StateCodes)):
            for j in range(0, len(month_list)):
                currState = code_to_state[StateCodes[i]]
                dx = db[(db['month'] == year_month[j]) & (db['state'] == currState)]
                num =  int(dx['totals'])
                totalBackgroundChecks[i] += num



    trace = [

        go.Choropleth(
        colorscale = scl,
                autocolorscale = False,
                locations =  StateCodes,
                z =  totalBackgroundChecks,
                text = list(state_to_code.keys()),
                locationmode='USA-states',
                marker=dict(
                    line=dict(
                        color='rgb(255,255,255)',
                        width=2
                    )),
                # colorbar=dict(
                #     title="Total Background Checks")


        )]




    return {
        'data': trace,
        'layout': go.Layout(
            title = 'US Background Checks ' + str(selected_year) + '<br>' + '(Total Background Checks)',
            width = 600,
            height = 600,
            geo = dict(
                scope = 'usa',
                projection = dict (type= 'albers usa'),
                showlakes = True,
                lakecolor = 'rgb(255,255,255)',
                    )
                    )
            }





# State provisions choropleth
@app.callback(Output('graph-with-slider', 'figure'),
             [Input('year-picker','value')])
def update_figure(selected_year):

    # filtered_df becomes a subset of the main df and contains all the
    # data but only for the selected year


    filtered_df = df[df['year'] == selected_year]

    # treat the filtered_df like the df in the original version since
    # it has the relevant data for the year and should produce the correct
    # graph
    #  df -> filtered_df=

    year_list = []
    for col in filtered_df.columns:
        filtered_df[col] = filtered_df[col].astype(str)
        year_list.append(selected_year)

    filtered_df['text'] = filtered_df['state']
   


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
                #     title="Total Laws")
            )],
        'layout': go.Layout(
            title = 'US Firearms Provisions by State for '+ str(selected_year)  + '<br>' + '(Total Laws)',
            width = 600,
            height = 600,
            geo = dict(
                scope = 'usa',
                projection = dict (type= 'albers usa'),
                showlakes = True,
                lakecolor = 'rgb(255,255,255)',
            )



        )




        }



# Causes the table to update laws displayed
@app.callback(Output('provisions', 'children'),
                [Input('graph-with-slider','hoverData')])
def find_density(hoverData):

    code = hoverData['points'][0]['location']
    year = hoverData['points'][0]['customdata']




    test = df[(df['code'] == code) & (df['year'] == year)]

    Title = code_to_state[code] + ' Laws ' + str(year)

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

    lawsInStateDF = lawsInStateDF.rename(index=str, columns={"Category Code.1": "Category", "Category Code.2": "Type", "Category Code.3": "Abbrieviation", "Category Code.4": "Description" })




    return generate_table(lawsInStateDF,Title)


# mass-shooting scatter
@app.callback(Output('mass-shooting-scatter', 'figure'),
                [Input('year-picker','value')])
def massShootingScatter(selected_year):

    # location is the abbrieviation for the state


    year = selected_year

    monthVict = [0,0,0,0,0,0,0,0,0,0,0,0]
    monthDesc = []
    for i in range(1, 13):
        monthDesc.append('')


    for i in range(0, len(years)):
        if years[i] == year:
            Date = date[i]
            if Date[1] == '/':

                if Date[0] == '1':
                    monthVict[0] += int(totalVic[i])
                    monthDesc[0] += (desc[i] + '<br>')

                if Date[0] == '2':
                    monthVict[1] += int(totalVic[i])
                    monthDesc[1] += (desc[i] + '<br>')

                if Date[0] == '3':
                    monthVict[2] += int(totalVic[i])
                    monthDesc[2] += (desc[i] + '<br>')

                if Date[0] == '4':
                    monthVict[3] += int(totalVic[i])
                    monthDesc[3] += (desc[i] + '<br>')

                if Date[0] == '5':
                    monthVict[4] += int(totalVic[i])
                    monthDesc[4] += (desc[i] + '<br>')

                if Date[0] == '6':
                    monthVict[5] += int(totalVic[i])
                    monthDesc[5] += (desc[i] + '<br>')

                if Date[0] == '7':
                    monthVict[6] += int(totalVic[i])
                    monthDesc[6] += (desc[i] + '<br>')

                if Date[0] == '8':
                    monthVict[6] += int(totalVic[i] )
                    monthDesc[6] += (desc[i] + '<br>')

                if Date[0] == '9':
                    monthVict[8] += int(totalVic[i])
                    monthDesc[8] += (desc[i] + '<br>')

            else:

                if Date[1] == '0':
                    monthVict[9] += int(totalVic[i])
                    monthDesc[9] += (desc[i] + '<br>')

                if Date[1] == '1':
                    monthVict[10] += int(totalVic[i])
                    monthDesc[10] += (desc[i] + '<br>')

                if Date[1] == '2':
                    monthVict[11] += int(totalVic[i])
                    monthDesc[11] += (desc[i] + '<br>')

    maxVict = max(monthVict)


    traces = []

    month_list = ['-01','-02', '-03', '-04', '-05', '-06', '-07','-08','-09','-10','-11','-12' ]
    year_month = []

    for i in month_list:
        curr = str(year) + i
        year_month.append(curr)

    traces.append(go.Scatter(
        x=monthes,
        y=monthVict,
        text= monthDesc,
        mode='markers',
        opacity=0.7,
        marker={'size': 15},
        name= 'Shootings',
        yaxis='Victims of mass shootings'
        ))



    return {
        'data': traces,
        'layout': go.Layout(

            title= str(year) + ' Mass Shootings',
            xaxis= {'title': 'Month'},
            yaxis = dict(range= [0,maxVict+5],autorange= True, title='Total Victims') ,
            hovermode='closet',
            legend=dict(orientation="v")

            )
    }









# background-check scatterplot
@app.callback(Output('background-scatter-lasso', 'figure'),
                [Input('year-picker','value')])
def backgroundScatterLasso(selected_year):

    # location is the abbrieviation for the state

    numOfStates = len(StateCodes)
    year = selected_year


    traces = []

    month_list = ['-01','-02', '-03', '-04', '-05', '-06', '-07','-08','-09','-10','-11','-12' ]
    year_month = []

    for i in month_list:
        curr = str(year) + i
        year_month.append(curr)




    if year < 1999:
        for i in range(0,numOfStates):
            Name = code_to_state[StateCodes[i]]
            temp = [0,0,0,0,0,0,0,0,0,0,0,0]
            traces.append(go.Scatter(
            x=monthes,
            y=temp,
            text=' ' + Name,
            mode='lines+markers',
            opacity=0.7,
            marker={'size': 15},
            name=Name,
            yaxis='Total Background Checks'
        ))




    else:
        for i in range(0,numOfStates):
            dx = db[(db.month.isin(year_month)) & (db.state == code_to_state[StateCodes[i]])]
            dx = dx.iloc[::-1]
            Name = code_to_state[StateCodes[i]]


            traces.append(go.Scatter(
            x=monthes,
            y=dx['totals'],
            text= Name,
            mode='lines+markers',
            opacity=0.7,
            marker={'size': 15},
            name=Name,
            yaxis='Total Background Checks'
            ))



    return {
        'data': traces,
        'layout': go.Layout(

            title= str(selected_year) + ' background checks',
            xaxis= {'title': 'Month'},
            yaxis = dict(range= [0,600000],autorange= True, title='Total Background Checks') ,
            hovermode='closet',
            legend=dict(orientation="v")

            )
    }

@app.callback(Output('shooting_locations', 'figure'),
             [Input('shooting_range','value')])
def update_locations(selected_years):
    # selected_years is a list


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
	app.run_server()
