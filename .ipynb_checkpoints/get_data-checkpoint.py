# Import libraries needed
import pandas as pd
import yfinance as yf

# This function takes all tickers (including stocks, cryptocurrencies and indexes), and returns a pandas dataframe of their historical OHLC prices
def get_data(ticker1, ticker2, start_date, end_date):
    # Put all tickers in a string seperated by space
    tickers = f'{ticker1} {ticker2}'
    
    # Get data from Yahoo Finance and assign it to a pandas dataframe
    df = yf.download(tickers, start=start_date, end=end_date)
    
    # Return the pandas dataframe
    return df    
 