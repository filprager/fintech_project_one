# Import libraries needed
import pandas as pd

def process_data(df, tickers, weights):
    # Extract all tickers' closing prices from the given dataframe 
    closing_prices = pd.DataFrame()

    for ticker in tickers:
        closing_prices[ticker] = df[ticker]['close']

    # Calculate all tickers' daily returns
    daily_returns_tickers = closing_prices.pct_change()

    # Calculate portfolio's daily returns
    daily_returns_portfolio = daily_returns_tickers.dot(weights)

    # Calculate portfolio's cumulative returns
    cumulative_returns_portfolio = (1 + daily_returns_portfolio).cumprod() - 1

    # Convert portfolio's cumulative returns to a pandas dataframe
    cumulative_returns_portfolio_df = pd.DataFrame()
    cumulative_returns_portfolio_df['Cumulative Returns'] = cumulative_returns_portfolio

    return cumulative_returns_portfolio_df