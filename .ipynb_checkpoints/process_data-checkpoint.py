# Import libraries needed
import os
import requests
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation
import json


def process_data_cumulative_returns(df, tickers, weights):
    # Extract all tickers' closing prices from the given dataframe 
    closing_prices = pd.DataFrame()

    for ticker in tickers:
        closing_prices[ticker] = df[ticker]['close']

    # Calculate all tickers' daily returns
    daily_returns_tickers = closing_prices.pct_change()

    # Calculate portfolio's daily returns based on ticker weighting
    daily_returns_portfolio = daily_returns_tickers.dot(weights)

    # Calculate portfolio's cumulative returns
    cumulative_returns_portfolio = (1 + daily_returns_portfolio).cumprod() - 1

    # Convert portfolio's cumulative returns to a pandas dataframe
    cumulative_returns_portfolio_df = pd.DataFrame()
    cumulative_returns_portfolio_df['Cumulative Returns'] = cumulative_returns_portfolio

    return cumulative_returns_portfolio_df


def process_data_monte_carlo(df, weights):
    # Configuring a Monte Carlo simulation to forecast 10 years cumulative returns
    monte_carlo_df = MCSimulation(
        portfolio_data = df,
        weights = weights,
        num_simulation = 5,
        num_trading_days = 252*10
    )
    
    # Running the Monte Carlo simulation to forecast 10 years cumulative returns
    #monte_carlo_df = monte_carlo_ten_year.calc_cumulative_return()

    return monte_carlo_df