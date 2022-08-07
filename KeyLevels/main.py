
import plotly.graph_objects as go
import pandas as pd 
data = pd.read_csv('../Data/EURUSD.csv')


fig = go.Figure(data=[go.Candlestick(x=data['date'],
                open=data['open'],
                high=data['high'],
                low=data['low'],
                close=data['close'])])


data['levels']  = data['close'][
  (data['close'].shift(1) < data['close']) &
  (data['close'].shift(-1) < data['close']) |
  (data['close'].shift(1) > data['close']) &
  (data['close'].shift(-1) > data['close'])
]


data['levels_2']  = data['close'][
  (data['close'].shift(2) < data['close']) &
  (data['close'].shift(-2) < data['close']) |
  (data['close'].shift(2) > data['close']) &
  (data['close'].shift(-2) > data['close'])
]

data = data[(data['levels'].notna()) & (data['levels_2'].notna())]

fig.add_trace(go.Scatter(
    x=data['date'],
    y=data['levels'],
    mode="markers",
    marker = {'color' : 'blue'},
    name='key levels'
))


fig.show()

