# %%
import yfinance
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# %%
df = pd.read_csv('./Tickers_info.csv', encoding_errors='ignore')
df.sort_values(by='Name', inplace=True)
df.set_index('Name', inplace=True)
df.head()

# %%
# nifty = yfinance.Ticker('^NSEI')
# nifty.info
# df_nifty = nifty.history(period='1d', interval='5m',rounding=True)
# df_nifty.head()
# fig = go.Figure()
# fig.add_trace(go.Candlestick(x= df.index, open=df_nifty['Open'], high=df_nifty['High'], low=df_nifty['Low'], close=df_nifty['Close']))
# fig.update_layout(title='NIFTY50')
# fig.update_layout(xaxis_rangeslider_visible=False)
# fig.show()

# fig_line = go.Figure()
# fig_line.add_trace(go.Scatter(x=df_nifty.index, y=df_nifty['Close']))
# fig_line.update_layout(title='NIFTY50')
# fig_line.update_traces(mode = 'lines')
# fig_line.show()

# %%
# df.index

# %%
# for x in df.index:
#     print(df.loc[x,'Ticker'])

# %%
app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': df.loc[i, 'Ticker']} for i in df.index],
    ),
    dcc.Graph(id='Candle_chart'),
])

# %%


@app.callback(
    Output('Candle_chart', 'figure'),
    [Input('dropdown', 'value')])
# [Input('dropdown','value'),Input()])
def update_scrip(val):

    scrip = yfinance.Ticker(val)
    df_scrip = scrip.history(period='1d', interval='5m', rounding=True)

    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df_scrip.index,
                  open=df_scrip['Open'], high=df_scrip['High'], low=df_scrip['Low'], close=df_scrip['Close']))
    fig.update_layout(template='plotly_white')
    fig.update_layout(title=val)
    fig.update_layout(xaxis_rangeslider_visible=False)
    return fig


# %%
if __name__ == '__main__':
    app.run_server()

# %%
# scrip = yfinance.Ticker('FSL.NS')
# df_scrip = scrip.history(period='1d', interval='5m',rounding=True)
# df_scrip.head()
# fig = go.Figure()
# fig.add_trace(go.Candlestick(x= df_scrip.index, open=df_scrip['Open'], high=df_scrip['High'], low=df_scrip['Low'], close=df_scrip['Close']))
# fig.update_layout(title='val')
# fig.show()
