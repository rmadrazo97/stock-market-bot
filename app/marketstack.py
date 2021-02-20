import os
import requests
import json

# API_KEY = os.environ.get("MARKET_STACK_KEY")
API_KEY = "8d1135a2ee709d14fd9a5ab1d32faed9"
BASE_URL= "http://api.marketstack.com/v1/"

def get_stock_price(stock_symbol):
    params = {
        'access_key': API_KEY
    }
    end_point = ''.join([BASE_URL,"tickers/", stock_symbol ,"/intraday/latest"])
    api_result = requests.get(end_point,params)
    json_result = json.loads(api_result.text)
    return {
        # "last_price": json_result['last'],
        "full_res":json_result
    }

# result = get_stock_price("AAPL")
# print(result)