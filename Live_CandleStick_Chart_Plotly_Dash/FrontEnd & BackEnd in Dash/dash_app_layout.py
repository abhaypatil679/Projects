from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from json import load

with open('./nifty_500_tickers_yfinance.json', 'rt') as json_file:
    nifty_500_tickers = load(json_file)


result_features = ['Total Revenue Qtr cr',
                   'Operating Expenses Qtr Cr',
                   'Operating Profit Qtr Cr',
                   'Depreciation Qtr Cr',
                   'Interest Qtr Cr',
                   'Profit Before Tax Qtr Cr',
                   'Tax Qtr Cr',
                   'Net Profit Qtr Cr',]

container = html.Div(className='container', id='container')

row1 = html.Div(className='row', style={'margin-top': '30px'},
                children=[html.Div(className='col-6',
                                   children=dcc.Dropdown(id='drop_scrip',
                                                         options=[{'label': company_name, 'value': company_name} for company_name in nifty_500_tickers.keys()],
                                                         value='Aditya Birla Capital Ltd.',
                                                         clearable=False)),
                          ],
                )

row2 = html.Div(className='row',
                children=dcc.Loading(id='loading-1', type='default',
                                     children=dcc.Graph(id='candle_stick_chart')))
row3 = html.Div(className='row',
                children=[html.Div(className='col-4',
                                   children=dcc.Dropdown(id='drop_left',
                                                         options=[{'label': res, 'value': res} for res in result_features],
                                                         value='Total Revenue Qtr cr',
                                                         clearable=False)),
                          html.Div(className='col-4',
                                   children=dcc.Dropdown(id='drop_right',
                                                         options=[{'label': res, 'value': res} for res in result_features],
                                                         value='Net Profit Qtr Cr',
                                                         clearable=False)),
                          ],
                )
row4 = html.Div(className='row',
                children=dcc.Loading(id='loading-2', type='default',
                                     children=dcc.Graph(id='bar_chart')))


container.children = [row1,row2,html.Hr(),row3,row4]

