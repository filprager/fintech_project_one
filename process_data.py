# Import libraries needed
import os
import requests
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation
import json


def process_data_cumulative_returns(df, tickers, weights, raw_data_market):
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
    cumulative_returns_portfolio_df['Portfolio'] = cumulative_returns_portfolio
    
    # Calculate all tickers' cumulative returns
    cumulative_returns_tickers = (1 + daily_returns_tickers).cumprod() - 1
    
    # Combine the tickers' cumulative with the portfolio's cumulative return into one DataFrame
    cumulative_returns_combined = cumulative_returns_tickers
    cumulative_returns_combined['Portfolio'] = cumulative_returns_portfolio_df
    
    # Calculate cumulative return of the marekt i.e. SPY
    closing_prices_market = raw_data_market['SPY']['close']
    daily_returns_market = closing_prices_market.pct_change()
    cumulative_returns_market = (1 + daily_returns_market).cumprod() - 1
    
    # Combine the cumulative return of the tickers, portfolio and market
    cumulative_returns_combined['Market'] = cumulative_returns_market

    return cumulative_returns_combined


def process_data_monte_carlo(df, weights):
    # Configuring a Monte Carlo simulation to forecast 10 years cumulative returns
    monte_carlo_config = MCSimulation(
        portfolio_data = df,
        weights = weights,
        num_simulation = 10,
        num_trading_days = 252*10
    )
    
    # Running the Monte Carlo simulation to forecast 10 years cumulative returns
    monte_carlo_df = monte_carlo_config.calc_cumulative_return()

    return monte_carlo_df

def process_data_monte_carlo_summary(df, weights):
    # Configuring a Monte Carlo simulation to forecast 10 years cumulative returns
    monte_carlo_config = MCSimulation(
        portfolio_data = df,
        weights = weights,
        num_simulation = 10,
        num_trading_days = 252*10
    )
    
    # Fetch summary statistics from the Monte Carlo simulation results
    summary_table = monte_carlo_config.summarize_cumulative_return()
    
    ## Calculate the expected portfolio return at the 95% lower and upper confidence intervals based on a $1000 initial investment
    
    # Set initial investment
    initial_investment = 1000

    # Use the lower and upper `95%` confidence intervals to calculate the range of the possible outcomes of the initial investment
    ci_lower = round(summary_table[8]*initial_investment,2)
    ci_upper = round(summary_table[9]*initial_investment,2)

    # Prepare results for print
    portfolio_return_summary = (f"There is a 95% chance that an initial investment of ${initial_investment} in the portfolio"
                                f" over the next 10 years will end within the range of"
                                f" ${ci_lower} and ${ci_upper}")
    
    return portfolio_return_summary