#!/usr/bin/python
import plotly.graph_objs as go
import pandas as pd
import math
from flask import Flask, request, render_template
"""This file launches a Flask server app wich serves html and JavaScript pages.  
It takes in a dataset and filters movie data by genre.  When a request is sent to
the server, it returns a filtered set of data from the dataset."""

df = pd.read_csv('https://raw.githubusercontent.com/WigodskyD/data-sets/master/NYC_Map_Data.csv')
df.columns.values[0] = 'index'

#----------------------------------
#This is the first of two functions used later for filtering.
#choose genre


def filter_genre(genre, datafr=df):
    genre_filter = genre[0:3]
    filterer = datafr['movies_genre'].str.contains(genre_filter)
    df_filtered = datafr[filterer]
    return df_filtered



#----------------------------------
#choose year

#This is the second filtering function.

def filter_year(year, datafr=df):
    year_set = int(math.floor(year/10)*10)
    year_set_bool = datafr['movies_year'] - year_set < 10
    df_filtered_yr = datafr[year_set_bool]
    year_set_bool = df_filtered_yr['movies_year'] - year_set > -1
    df_filtered_yr = df_filtered_yr[year_set_bool]
    return df_filtered_yr



#----------------------------------
#This section makes lists of latitudes and longitudes to send to Plotly.
latitude = list(df['movies_lat'])
longitude = list(df['movies_long'])
movie_names = list(df['movies_names'])


#This is the first attempt at creating a graph.  It doesn't contain real locations from our data.
trace=dict(
    locationmode="USA-states",
    type='scattergeo',
    lon=[-73.9712, -73.9442], lat=[40.7831, 40.6782],
    mode='markers')

#py.plot([trace], filename='NYC_map')

mapbox_access_token = 'pk.eyJ1IjoiZGFud2lnIiwiYSI6ImNqcDdvamp0dTB2cmYza3FzeDN3ZW05OGEifQ.OzM_HzpiAcFeJLb21l2xPA'

#The following returns a Plotly plot.  It can filter the data and create a separate graph on Plotly's
#site.  It is not callable within an html page.  The live graphs will be called from a JavaScript JQuery function.
data = [
    go.Scattermapbox(
        lat=latitude,
        lon=longitude,
        mode='markers',
        marker=dict(
            size=14
        ),
        text=movie_names,
    )
]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40.7638,
            lon=-73.9795
        ),
        pitch=0,
        zoom=10
    ),
)

fig = dict(data=data, layout=layout)
config= {'displayModeBar': False, 'scrollZoom': True}
#py.plot(fig, filename='NYC_map', config=config)




#------------------------------------------------------------------
"""The Flask Server app starts here."""
app = Flask(__name__)

#@app.route('/')


@app.route('/interactive')

def interactive():
    """This function creates the webpage by serving the html/css/JavaScript file"""
    return render_template("server_pageg.html")

@app.route('/_background_process', methods=['GET', 'POST'])
def get_data():
    """This function receives data from the page and returns a filtered set of data."""
    genre=request.args.get('passed_genre')
    genre=str(genre)
    decade=request.args.get('passed_decade')
    decade=int(decade)
    dfb=df
    if genre:
        dfb = filter_genre(genre, dfb)
    if not (decade == 0):
        dfb = filter_year(decade, dfb)
    print(genre)
    return dfb.to_json()