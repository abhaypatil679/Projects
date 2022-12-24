from yfinance import Ticker
from dash import Dash, Input, Output, State
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_app_layout import container
from json import load
import pandas as pd

with open('./nifty_500_tickers_yfinance.json', 'rt') as json_file:
    nifty_500_tickers = load(json_file)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = container


@app.callback(
    [Output('candle_stick_chart', 'figure'), Output('bar_chart', 'figure')],
    [Input('drop_scrip', 'value'),
     Input('drop_left', 'value'), Input('drop_right', 'value')],)
def update_graph(company_name, res_left, res_right):
    scrip = Ticker(nifty_500_tickers[company_name])
    df_scrip = scrip.history(interval='1d', start='2020-01-01', rounding=True)

    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df_scrip.index,
                  open=df_scrip['Open'], high=df_scrip['High'], low=df_scrip['Low'], close=df_scrip['Close']))

    fig.update_layout(template='gridon')
    # fig.update_layout(title=df_scrip.index[0].strftime(
    #     '%A, %d %B %Y        ') + company_name)
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_layout(yaxis_title='Share Price, INR')
    df = pd.read_csv(f'./nifty_500_scraped_data_processed/{company_name}.csv', index_col=0)

    fig_b = go.Figure()
    fig_b.add_bar(x=df.index, y=df[res_left], name=res_left)
    fig_b.add_bar(x=df.index, y=df[res_right], name=res_right)
    fig_b.update_layout(yaxis_title='Value, Cr')
    fig_b.update_layout(template='gridon')

    return [fig, fig_b]


if __name__ == '__main__':
    app.run()
