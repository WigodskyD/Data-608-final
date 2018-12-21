import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import math
from flask import Flask, request, render_template
df = pd.read_csv('https://raw.githubusercontent.com/WigodskyD/data-sets/master/NYC_Map_Data.csv')
df.columns.values[0] = 'index'
"""This file filters the movie database for points along a specific walk chosen beforehand"""
#----------------------------------
#choose genre
genre_filter = 'Act'
#80s movie walk filterer:
#filterer = df['index'].isin([59,60,19,25,38,213,195,54,55,69])
#Hollywood classics walk filterer:
filterer = df['index'].isin([124,2,21,22,121,209,181,166,119])
df_filtered = df[filterer]
latitude = list(df_filtered['movies_lat'])
longitude = list(df_filtered['movies_long'])
movie_names = list(df_filtered['movies_names'])

mapbox_access_token = 'pk.eyJ1IjoiZGFud2lnIiwiYSI6ImNqcDdvamp0dTB2cmYza3FzeDN3ZW05OGEifQ.OzM_HzpiAcFeJLb21l2xPA'

data = [
    go.Scattermapbox(
        lat=latitude,
        lon=longitude,
        mode='markers',
        marker=dict(
            size=11, color='darkcyan'
        ),
        text=movie_names,
    )
]

layout = go.Layout(
      autosize=False,
        height= 610,
        width= 680,
        margin=go.layout.Margin(l=0,r=0,t=0,b=0),
        hovermode='closest',
        mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40.728,
            lon=-73.99
        ),
        pitch=0,
        zoom=13
    ),
)

fig = dict(data=data, layout=layout)
config= {'displayModeBar': False, 'scrollZoom': True}
#plot turned off so as not to overwrite it
#py.plot(fig, filename='classics_movie_map', config=config)

