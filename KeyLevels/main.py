
import plotly.graph_objects as go
import pandas as pd 
import numpy as np
data = pd.read_csv('../Data/EURUSD.csv')

# print(data.head())



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

# print(data[data['levels_1'].notna()])
# print(data[data['levels_2'].notna()])
# print(len(data['levels_1'].notna()))
# print(len(data['levels_2'].notna()))


data = data[(data['levels'].notna()) & (data['levels_2'].notna())]
print(data)

data.fillna(0)




fig.add_trace(go.Scatter(
    x=data['date'],
    y=data['levels'],
    mode="markers",
    marker = {'color' : 'blue'},
    name='key levels'
))


fig.show()

