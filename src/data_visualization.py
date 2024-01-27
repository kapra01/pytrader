
# To bypass making API calls which we are limited by, we will be creating dummy OHLCV dataframes as below

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
# Calculate SMA and MACD
df['SMA'] = df['C'].rolling(window=20).mean()
short_ema = df['C'].ewm(span=12, adjust=False).mean()
long_ema = df['C'].ewm(span=26, adjust=False).mean()
df['MACD'] = short_ema - long_ema
df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()


# Plot for closing price and SMA

plt.figure(figsize=(10, 6))
plt.plot(df['C'], label='Close')
plt.plot(df['SMA'], label='20-day SMA')
plt.title('Close Price and SMA')
plt.legend()
plt.savefig('output/ClosePrice_and_SMA.png')


# Plot for MACD and Signal Line

plt.figure(figsize=(10, 6))
plt.plot(df['MACD'], label='MACD')
plt.plot(df['Signal_Line'], label='Signal Line')
plt.title('MACD and Signal Line')
plt.legend()
plt.savefig('output/MACD_and_SignalLine.png')

'''

def create_plot(df, title):
    plt.figure(figsize=(10, 6))
    for col in df.columns.tolist():
        plt.plot(df[col], label=col)
    plt.title(title)
    plt.legend()
    filepath = 'output/' + title.replace(' ','_')
    plt.savefig(filepath)
    plt.show()

'''
# Generate dummy OHLCV data

# Create a date range
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='B')  # Business days

np.random.seed(0)  # For reproducible results
data = {
    'O': np.random.rand(len(dates)) * 100,
    'H': np.random.rand(len(dates)) * 100,
    'L': np.random.rand(len(dates)) * 100,
    'C': np.random.rand(len(dates)) * 100,
    'V': np.random.rand(len(dates)) * 1000
}
df = pd.DataFrame(data, index=dates)

'''
