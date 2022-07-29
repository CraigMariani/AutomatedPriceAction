from secret import Secret
import requests
import pandas as pd 


headers = {
    'Content-Type': 'application/json'
}

ticker = 'EURUSD'
requestResponse = requests.get("https://api.tiingo.com/tiingo/fx/prices?tickers={}&startDate=2022-07-28&resampleFreq=5min&token={}".format(ticker, Secret.api_key), 
                                headers=headers)

data = requestResponse.json()


df = pd.DataFrame.from_dict(data)
   
df.to_csv('Data/{}.csv'.format(ticker))
