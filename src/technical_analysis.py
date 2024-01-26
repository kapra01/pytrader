import pandas as pd

'''
Module to carry out SMA, EMA and MACD analysis of dataframes.

Strategies:

For SMA (Simple Moving Average). This smooths out price data by creating a constantly updated average price. 
It helps you see the overall trend of a stock's price, removing daily fluctuations. 
If the stock price is above the SMA, it might be in an uptrend; below the SMA could suggest a downtrend.
Note SMA gives equal weight to all points in the period, while EMA (Exponential Moving Average) gives more weight to recent prices.
For MACD. A common strategy is to buy when the MACD crosses above the Signal Line and sell when it crosses below.

We assume the dataframe has the column names of Open, High, Low, Close and Volume.

'''


def add_macd_to_df(df):
    # Calculate the Short-term Exponential Moving Average (EMA)
    df['12d_EMA'] = df['Close'].ewm(span=12, adjust=False).mean()
    # Calculate the Long-term EMA
    df['26d_EMA'] = df['Close'].ewm(span=26, adjust=False).mean()
    # Compute the MACD (12-day EMA - 26-day EMA)
    df['MACD'] = df['12d_EMA'] - df['26d_EMA']
    # Calculate the Signal Line (9-day EMA of the MACD)
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
    return df

def add_sma_to_df(df, period):
    periods = {'short': 20, 'medium': 50, 'long': 200}
    if period in periods:
        df[f'{periods[period]}d_SMA'] = df['Close'].rolling(window=periods[period]).mean()
    else:
        raise ValueError("Invalid period. Choose 'short', 'medium', or 'long'")
    return df

def add_ema_to_df(df, period):
    periods = {'short': 20, 'medium': 50, 'long': 200}
    if period in periods:
        df[f'{periods[period]}d_EMA'] = df['Close'].ewm(span=periods[period], adjust=False).mean()
    else:
        raise ValueError("Invalid period. Choose 'short', 'medium', or 'long'")
    return df

# Usage:
# df = add_sma_to_df(df, 'short')
# df = add_ema_to_df(df, 'medium')
