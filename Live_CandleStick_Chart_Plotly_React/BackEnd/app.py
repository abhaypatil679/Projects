from flask import Flask, render_template, request, Response
from yfinance import Ticker
from plotly.graph_objs._figure import Figure
from plotly.graph_objs._layout import Layout
from pandas import read_csv
from datetime import datetime

# main app instance
app = Flask(__name__, static_folder='assets')


@app.get('/')
def home_page():
    return render_template('index.html')


@app.get('/ticker')
def plolty_callback():
    ticker = request.args['ticker']
    period = request.args['period']
    scrip_name = request.args['scrip_name']
    scrip = Ticker(ticker)
    interval = {
        '1d': '5m',
        '2y': '1d'
    }
    df_scrip = scrip.history(period=period, interval=interval[period], rounding=True)
    # df_scrip = scrip.history(period='1d', start='2020-01-01', rounding=True)

    fig_candle = Figure()
    layout = Layout()
    fig_candle.add_candlestick(x=df_scrip.index,
                               open=df_scrip['Open'],
                               high=df_scrip['High'],
                               low=df_scrip['Low'],
                               close=df_scrip['Close'])

    layout.title = scrip_name + df_scrip.index[0].strftime('<br>%A, %d %B %Y')
    layout.title.font.size = 18
    layout.title.font.family = 'Cambria'
    layout.template = 'gridon'
    layout.xaxis.rangeslider.visible = False
    layout.yaxis.title = 'Share Price, INR'
    layout.height = 400

    if period == '1d':
        start = datetime.strptime('2022-12-26 09:00:00', '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime('2022-12-26 15:30:00', '%Y-%m-%d %H:%M:%S')
        layout.xaxis.range = [start, end]

    fig_candle.layout = layout
    return Response(fig_candle.to_json(), mimetype='application/json', headers={'Access-Control-Allow-Origin': '*'})  # for fig_candle.to_html(include_plotlyjs='cdn')


@app.get('/bar')
def update_bar_left():
    if request.args:
        pass
        # print(f"you passed {request.args}")
    else:
        return "no data was passed! to dropdowns"

    left_dropdown_value = request.args['left_dropdown_value']
    right_dropdown_value = request.args['right_dropdown_value']
    scrip_name = request.args['scrip_name']

    df = read_csv(f'./nifty_500_scraped_data_processed/{scrip_name}.csv', index_col=0)

    fig_bar = Figure()
    fig_bar.add_bar(x=df.index, y=df[left_dropdown_value], name=left_dropdown_value)
    fig_bar.add_bar(x=df.index, y=df[right_dropdown_value], name=right_dropdown_value)

    layout = Layout()
    layout.title = scrip_name+' Quaterly Results <br>' + f'{left_dropdown_value} vs {right_dropdown_value}'
    layout.title.font.size = 18
    layout.title.font.family = 'Cambria'
    layout.yaxis.title = 'Value, Cr'
    layout.xaxis.title = 'Quaterly Results'
    layout.template = 'none'
    layout.height = 400

    fig_bar.layout = layout
    return Response(fig_bar.to_json(), mimetype='application/json', headers={'Access-Control-Allow-Origin': '*'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
