import os
import datetime as dt
import time

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event

import plotly.plotly as py
from plotly.graph_objs import *

import numpy as np
from scipy.stats import rayleigh

from tinydb import TinyDB, Query

from flask import Flask, send_from_directory


server = Flask('BitcoinMAvgs')
app = dash.Dash('BitcoinMAvgs-App', serer=server, url_base_pathname='/dash/', csrf_protect=False)

app.layout = html.Div([

    html.Div([
        html.H2("Bitcoin prices with moving averages")
    ], className='banner'),

    html.Div([

        html.Div([
            html.H3("Price(USD) " + str(dt.datetime.now().date()))
        ], className='Title'),

        html.Div([
            dcc.Graph(id='bpi')
        ], className='twelve columns bpi'),

        dcc.Interval(id='bpi-update', interval=12000)

    ], className='row bpi-row'),


    html.Div([
        html.P("Period"),
        dcc.Dropdown(id='period',
            options = [{'label': i, 'value': i} for i in ['5', '10', '15']], 
            value='10'
        )
    ], style={'width': '31%', 'display': 'inline-block'}),

    html.Div([
        html.P("Box plot Period"),
        dcc.Dropdown(id='box_plot_period',
            options=[{'label': i, 'value': i} for i in ['5', '10', '15']],
            value='10'
        )
    ], style={'width': '31%', 'margin-left': '3%', 'display': 'inline-block'}),

    html.Div([
        html.P("Time frame"),
        dcc.Dropdown(id='timeframe',
            options=[{'label': i, 'value': i} for i in ['1', '2', '3', '4']],
            value='2'
        )
    ], style={'width': '31%', 'float': 'right', 'display': 'inline-block'})

], className='main-div')







if __name__ == '__main__':
    app.run_server(debug=True)
