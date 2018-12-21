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
"""This file filters the movie database and colors it based on the most common genre options: Comedy, Action,
 Adventure, Sci-Fi, Crime, Drama, Family, Musical, Western"""
#----------------------------------
#choose genre


def filter_genre(genre, datafr=df):
    genre_filter = genre[0:3]
    filterer = datafr['movies_genre'].str.contains(genre_filter)
    df_filtered = datafr[filterer]
    return df_filtered



#----------------------------------
#choose year


def filter_year(year, datafr=df):
    year_set = int(math.floor(year/10)*10)
    year_set_bool = datafr['movies_year'] - year_set < 10
    df_filtered_yr = datafr[year_set_bool]
    year_set_bool = df_filtered_yr['movies_year'] - year_set > -1
    df_filtered_yr = df_filtered_yr[year_set_bool]
    return df_filtered_yr



#----------------------------------

latitude = list(df['movies_lat'])
longitude = list(df['movies_long'])
movie_names = list(df['movies_names'])



trace=dict(
    locationmode="USA-states",
    type='scattergeo',
    lon=[-73.9712, -73.9442], lat=[40.7831, 40.6782],
    mode='markers')

#py.plot([trace], filename='NYC_map')

#------------------Filter Points By Genre--------------------------------------
dfComedy = filter_genre('Comedy')
dfAction = filter_genre('Action')
dfAdventure = filter_genre('Adventure')
dfScifi = filter_genre('Sci-Fi')
dfCrime = filter_genre('Crime')
dfDrama = filter_genre('Drama')
dfFamily = filter_genre('Family')
dfMusical = filter_genre('Musical')
dfWestern = filter_genre('Western')

latitudeCom = list(dfComedy['movies_lat'])
longitudeCom = list(dfComedy['movies_long'])
latitudeAct = list(dfAction['movies_lat'])
longitudeAct = list(dfAction['movies_long'])
latitudeAdv = list(dfAdventure['movies_lat'])
longitudeAdv = list(dfAdventure['movies_long'])
latitudeSci = list(dfScifi['movies_lat'])
longitudeSci = list(dfScifi['movies_long'])
latitudeCri = list(dfCrime['movies_lat'])
longitudeCri = list(dfCrime['movies_long'])
latitudeDra = list(dfDrama['movies_lat'])
longitudeDra = list(dfDrama['movies_long'])
latitudeFam = list(dfFamily['movies_lat'])
longitudeFam = list(dfFamily['movies_long'])
latitudeMus = list(dfMusical['movies_lat'])
longitudeMus = list(dfMusical['movies_long'])
latitudeWes = list(dfWestern['movies_lat'])
longitudeWes = list(dfWestern['movies_long'])


#------------------------------------------------------------------------------


mapbox_access_token = 'pk.eyJ1IjoiZGFud2lnIiwiYSI6ImNqcDdvamp0dTB2cmYza3FzeDN3ZW05OGEifQ.OzM_HzpiAcFeJLb21l2xPA'

trace1=go.Scattermapbox(
        lat=latitudeCom,
        lon=longitudeCom,
        mode='markers',
        marker=dict(
            size=11, color='coral'
        ),
        text=movie_names,
        name="comedy"
    )
trace2=go.Scattermapbox(
        lat=latitudeAct,
        lon=longitudeAct,
        mode='markers',
        marker=dict(
            size=11, color='mediumvioletred'
        ),
        text=movie_names,
        name="action"
    )
trace3=go.Scattermapbox(
        lat=latitudeAdv,
        lon=longitudeAdv,
        mode='markers',
        marker=dict(
            size=11, color='olivedrab'
        ),
        text=movie_names,
        name="adventure"
    )
trace4=go.Scattermapbox(
        lat=latitudeSci,
        lon=longitudeSci,
        mode='markers',
        marker=dict(
            size=11, color='chartreuse'
        ),
        text=movie_names,
        name="sci-fi"
    )
trace5=go.Scattermapbox(
        lat=latitudeCri,
        lon=longitudeCri,
        mode='markers',
        marker=dict(
            size=11, color='crimson'
        ),
        text=movie_names,
        name='crime'
    )
trace6=go.Scattermapbox(
        lat=latitudeDra,
        lon=longitudeDra,
        mode='markers',
        marker=dict(
            size=11, color='aqua'
        ),
        text=movie_names,
        name='drama'
    )
trace7=go.Scattermapbox(
        lat=latitudeFam,
        lon=longitudeFam,
        mode='markers',
        marker=dict(
            size=11, color='darkslategray'
        ),
        text=movie_names,
        name='family'
    )
trace8=go.Scattermapbox(
        lat=latitudeMus,
        lon=longitudeMus,
        mode='markers',
        marker=dict(
            size=11, color='mediumblue'
        ),
        text=movie_names,
        name='musical'
    )
trace9=go.Scattermapbox(
        lat=latitudeWes,
        lon=longitudeWes,
        mode='markers',
        marker=dict(
            size=11, color='darkkhaki'
        ),
        text=movie_names,
        name='western'
    )
data=[trace6,trace1,trace2,trace3,trace4,trace5,trace7,trace8,trace9]

layout = go.Layout(
    autosize=False,
    height=665,
    width=580,
    margin=go.layout.Margin(l=0,r=0,t=0,b=0),
    legend=dict(x=0,y=0),
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40.7638,
            lon=-73.9795
        ),
        pitch=0,
        zoom=12
    ),
)

fig = dict(data=data, layout=layout)
config= {'displayModeBar': False, 'scrollZoom': True}
py.plot(fig, filename='NYC_map', config=config)



#dfb = filter_genre('Fantasy')
#dfb = filter_year(1989, dfb)
#print(dfb['movies_year'])
#print(dfb['movies_genre'])
#print(dfb['movies_names'])
#print(dfb.to_json())