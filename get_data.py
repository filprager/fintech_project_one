# Import libraries needed
from dotenv import load_dotenv
import os
import pandas as pd
import alpaca_trade_api

def get_data(tickers, weights):
    # Load .env file
    load_dotenv()
    
    # Set buy time
    buy_time = pd.Timestamp("2020-07-14", tz="America/New_York").isoformat()

    # Set sell time
    sell_time = pd.Timestamp("2020-12-15", tz="America/New_York").isoformat()

    # Get data from Alpaca

    # Set Alpaca API key and secret
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    # Create the Alpaca API object
    alpaca = alpaca_trade_api.REST(alpaca_api_key, alpaca_secret_key)

    # Set the timeframe that stock data will be based on
    timeframe = "1D"

    # Get data for tickers
    df = alpaca.get_barset(
        tickers,
        timeframe,
        start = buy_time,
        end = sell_time
    ).df
    return df    