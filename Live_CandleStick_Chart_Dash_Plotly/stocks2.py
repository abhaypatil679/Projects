#app url: http://www.tradewihtnifty.ml

import yfinance
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv('./Tickers_info.csv', encoding_errors='ignore')
# df.sort_values(by='Name', inplace=True)
df.set_index('Name', inplace=True)
# df.head()

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='dropdown_top',
            options=[{'label': i, 'value': i} for i in df.index],
            value='Nifty 50',
            clearable=False
        )], style={'width': '30%', 'margin-left': '75px', 'margin-top': '30px'}),
    dcc.Graph(id='Candle_chart_top'),

    html.Div([
        dcc.Dropdown(
            id='dropdown_bottom',
            options=[{'label': i, 'value': i} for i in df.index],
            value='Sensex 30',
            clearable=False
        )], style={'width': '30%', 'margin-left': '75px', 'margin-top': '30px'}),
    dcc.Graph(id='Candle_chart_bottom'),
])


@app.callback(
    Output('Candle_chart_top', 'figure'),
    [Input('dropdown_top', 'value')])
# [Input('dropdown','value'),Input()])
def update_scrip_top(val):

    scrip = yfinance.Ticker(df.loc[val, 'Ticker'])
    df_scrip = scrip.history(period='1d', interval='5m', rounding=True)

    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df_scrip.index,
                  open=df_scrip['Open'], high=df_scrip['High'], low=df_scrip['Low'], close=df_scrip['Close']))

    fig.update_layout(template='plotly_white')
    fig.update_layout(title=df_scrip.index[0].strftime(
        '%A, %d %B %Y        ') + val)
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_layout(xaxis=dict(tickmode='linear',
                      tick0=df_scrip.index[0], dtick=30*60*1000))
    fig.update_yaxes(tickmode='auto')

    return fig


@app.callback(
    Output('Candle_chart_bottom', 'figure'),
    [Input('dropdown_bottom', 'value')])
# [Input('dropdown','value'),Input()])
def update_scrip_bottom(val):

    scrip = yfinance.Ticker(df.loc[val, 'Ticker'])
    df_scrip = scrip.history(period='1d', interval='5m', rounding=True)

    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df_scrip.index,
                  open=df_scrip['Open'], high=df_scrip['High'], low=df_scrip['Low'], close=df_scrip['Close']))

    fig.update_layout(template='plotly_white')
    fig.update_layout(title=df_scrip.index[0].strftime(
        '%A, %d %B %Y        ') + val)
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_layout(xaxis=dict(tickmode='linear',
                      tick0=df_scrip.index[0], dtick=30*60*1000))
    fig.update_yaxes(tickmode='auto')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
