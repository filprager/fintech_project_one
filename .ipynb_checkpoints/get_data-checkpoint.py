# Import libraries needed
from dotenv import load_dotenv
import os
import pandas as pd
import alpaca_trade_api

# Create a function to get stock data for given tickers, buy time and sell time
def get_data_stock(tickers, 
                   start_date,
                   end_date
                  ):
    
    # Load .env file
    load_dotenv()

    # Set Alpaca API key and secret
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    # Create the Alpaca API object
    alpaca = alpaca_trade_api.REST(alpaca_api_key, alpaca_secret_key)

    # Set the timeframe that stock data will be based on
    timeframe = "1D"
    
    # Convert start_date and end_date to proper time format
    start_date_formatted = pd.Timestamp(start_date, tz="America/New_York").isoformat()
    end_date_formatted = pd.Timestamp(end_date, tz="America/New_York").isoformat()

    # Get the data from Alpaca API
    df = alpaca.get_barset(
        tickers,
        timeframe=timeframe,
        start = start_date_formatted,
        end = end_date_formatted
    ).df
    
    # Return the data
    return df    

# Create a function to get data of the market (S&P 500)
def get_data_market(buy_time=pd.Timestamp("2020-01-01", tz="America/New_York").isoformat(),
                    sell_time=None
                   ):
    
    # Load .env file
    load_dotenv()

    # Set Alpaca API key and secret
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    # Create the Alpaca API object
    alpaca = alpaca_trade_api.REST(alpaca_api_key, alpaca_secret_key)

    # Set the timeframe that stock data will be based on
    timeframe = "1D"

    # Get the data from Alpaca API
    df = alpaca.get_barset(
        # I haven't figured out how to get S&P 500 index data, I'm using SPY as an alternative for now
        'SPY',
        timeframe=timeframe,
        start = buy_time,
        end = sell_time
    ).df
    
    # Return the data
    return df  