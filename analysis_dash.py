# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event
import plotly.graph_objs as go
import pandas as pd
# import seaborn as sns
# import pypyodbc
# import MySQLdb
# import pymysql
# import pymssql
from datetime import datetime as dt
import datetime as DT

# virtualenv -p /usr/bin/python2.7 env1
# pip install dash==0.17.7
# pip install dash-renderer==0.7.3
# pip install dash-html-components==0.6.2
# pip install dash-core-components==0.5.3
# pip install plotly==2.0.12

app = dash.Dash()

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})


app.layout = html.Div(children=[
    html.Div(children=[
    html.H4(children='Analysis Dash'),
    
    
    html.Div(id='div_row1',children=[
    
        # Div Retention
        html.Div(id='div_retention', children=[
            html.P("Retention"),
            dcc.Dropdown(
            id="sel_percent",
            options=[
                {'label': 'As Percentage', 'value': True},
                {'label': 'As Absolute', 'value': False}

            ],
            value=False,
            multi=False
            ),
            dcc.Dropdown(
            id="sel_att_only",
            options=[
                {'label': 'Attendees Only', 'value': True},
                {'label': 'Bookings', 'value': False}

            ],
            value=False,
            multi=False
            ),
            dcc.Dropdown(
            id="sel_on_org",
            options=[
                {'label': 'Match on Organisation', 'value': True},
                {'label': 'Match on Individual', 'value': False}

            ],
            value=False,
            multi=False
            ),
            dcc.Graph(
                id='retention-graph',
                # figure=get_retention_fig(attended_only=False,pcent=False, by_organisation=True)
                figure={
                'data': {'x':["a","b","c"],'y':[10,20,5]},
                'layout': {
                    'title': 'Placeholder Figure', 'xaxis':{'title':'Placeholder Figure'}, 'yaxis':{'title':'Placeholder Figure'}
                   }
                }
            )
        ], className='six columns'),

        # Div Bookings
        html.Div(id="div_bookings", children=[
            html.P("Bookings by Hour"),
            dcc.Dropdown(
            id="sel_date_filter",
            options=[
                {'label': 'Today', 'value': False},
                {'label': 'Last Seven Days', 'value': True}

            ],
            value=True,
            multi=False
            ),
            dcc.Graph(
                id='bookings_expo_7d-graph',
                figure={
                'data': {'x':["a","b","c"],'y':[10,20,5]},
                'layout': {
                    'title': 'Placeholder Figure', 'xaxis':{'title':'Placeholder Figure'}, 'yaxis':{'title':'Placeholder Figure'}
                   }
                }
                )
        ], className='six columns', style={'margin-top':'75'})

    ]),
    html.Div(id="div_row2", children=[
        html.Div(id="wyvern_sector", children=[
            html.P("Super Sector Wyvern"),
            # dcc.Dropdown(
            # id="sel_wv_name",
            # options=[{'label': i, 'value': i} for i in get_sel_names()],
            # value='NS_0017c2',
            # multi=False
            # ),
            dcc.Graph(
            id='super_sector_wv',
                figure={
                'data': {'x':["a","b","c"],'y':[10,20,5]},
                'layout': {
                    'title': 'Placeholder Figure', 'xaxis':{'title':'Placeholder Figure'}, 'yaxis':{'title':'Placeholder Figure'}
                   }
                }
            )


        ], className='six columns'),
        html.Div(id="row2_col2_ph", children=[
        html.P("Placeholder")], className='six columns') # , className='six columns'
    ]),

    ### refreshing interval, like invalidate later
    dcc.Interval(
        id='interval-component',
        interval=5*60*1000 # in milliseconds
    )
    ]),
    # html.Div(children=["text col A", "text col B"], style={'columnCount': 1})
    ])


# @app.callback(
#     Output(component_id='bookings_expo_7d-graph', component_property='figure'),
#     [Input(component_id='sel_date_filter', component_property='value')
#     ],
#     events=[Event('interval-component', 'interval')])
# def update(sel_date_filter):
#     # Make sure to add areguments above if using inputs... e.gr. def update(division, year):
#     figure = get_bookings_by_time_expo_fig(sel_date_filter)
#     return figure

# ## Updating Bookings EGU
# # @app.callback(
# #     Output(component_id='bookings_egu-graph', component_property='figure'),
# #     events=[Event('interval-component', 'interval')]
# # )
# # def update():
# #     figure = get_bookings_last_week_egu_fig()
# #     return figure

# ## Updating Retention

# @app.callback(
#     Output(component_id='retention-graph', component_property='figure'),
#     [Input(component_id='sel_percent', component_property='value'),
#     Input(component_id='sel_att_only', component_property='value'),
#     Input(component_id='sel_on_org', component_property='value')
#     ],
#     events=[Event('interval-component', 'interval')]
# )
# def update(sel_percent, sel_att_only, sel_on_org):
#     figure = get_retention_fig(attended_only=sel_att_only,pcent=sel_percent, by_organisation=sel_on_org)
#     return figure


# ## Updating Wyvern Chart

# @app.callback(
#     Output(component_id='super_sector_wv', component_property='figure'),
#     [Input(component_id='sel_wv_name', component_property='value')
#     ]
# )
# def update(sel_name):
#     print "Updating Wyvern Sector by input.", str(dt.now())
#     figure = get_wv_sel_sector_fig(sel_name)
#     return figure

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5083)