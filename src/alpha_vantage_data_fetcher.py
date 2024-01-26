import requests
import json
import pandas as pd
import os

"""
This script is designed to fetch, process and analyze financial data.
Currently, it only supports daily and weekly OHLCV data for a symbols.
TODO: Intraday support
"""


API_FUNCTION_TO_JSON_DATA_KEY = {
    'TIME_SERIES_DAILY' : 'Time Series (Daily)',
    'TIME_SERIES_WEEKLY' : 'Weekly Time Series'
}


def fetch_data(api_function, symbol=None):
    base_url = 'https://www.alphavantage.co/query'
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    # Add 'export ALPHA_VANTAGE_API_KEY=your_api_key' to your environment or .bashrc file
    params = {
        'function': api_function,
        'apikey': api_key
    }
    
    if symbol:
        params['symbol'] = symbol
    
    response = requests.get(base_url, params=params)
    return response.json()



def json_to_dataframe(json_data, api_function):
    # Convert JSON to DataFrame
    print(json_data)
    df = pd.DataFrame(json_data[API_FUNCTION_TO_JSON_DATA_KEY[api_function]]).transpose()
    #print(json_data)
    #df = pd.DataFrame(json_data['Time Series (Daily)']).transpose()
    df.index = pd.to_datetime(df.index)
    # Rename columns and other data cleaning steps
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume'] 
    # Sort in ascending index/time order
    df.sort_index(ascending=True, inplace=True)
    for col in df.columns:
        df[col] = df[col].astype(float)
    return df



def api_fetch_and_create_df(api_function, symbol):
    # Get api_function for symbol, compact datasize by default (last 100 datapoints)
    data = fetch_data(api_function, symbol)
    #print_json(data_ibm)
    # Get Global Market Open and Close statuses
    # data_mkt_status = fetch_data('MARKET_STATUS')
    # print_json(data_mkt_status)
    df_ibm = json_to_dataframe(data, api_function)
    return df_ibm

# Functions for debugging:

# Print neatly formatted JSON output
def print_json(json_data,indent=4):
    print(json.dumps(json_data, indent=indent))

# Print head and tail of Dataframe
def print_df(df):
    print("==== Head of DataFrame ====")
    print(df.head())
    print("\n==== Tail of DataFrame ====")
    print(df.tail())










