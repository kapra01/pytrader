import requests
import json
import os

base_url = 'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey='
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
# Add 'export ALPHA_VANTAGE_API_KEY=your_api_key' to your environment or .bashrc file

# Get Global Market Open and Close statuses

url = base_url + api_key
r = requests.get(url)
data_mkt_status = r.json()

# Tidier output with indent Vs just "print(data)"
print(json.dumps(data_mkt_status, indent=4))



"""
Another example API call:


# Get daily time series for IBM, compact datasize by default (last 100 datapoints)

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=xxxxxx'
r = requests.get(url)
data_ibm = r.json()

print(json.dumps(data_ibm, indent=4))

"""