# FinTech Project 1

## Project title

- Investor Analysis Tool (‘sleek name here’)
- My Portfolio

## Project description/outline

User inputs:

- Initial investment
- Stock/crypto tickers to compare (max 10 via free text field)
- Initial weight of each ticker (incl. sum check)
- Buy time
- Sell time
- Challenge - Enable/disable auto rebalance

App output:

- Past performance of the portfolio vs. the market
- Possible future best/worse performance of the \* portfolio vs. the market (Monte Carlo based)
- Risk level of the portfolio
- A pie chart of the initial weights
- A pie chart of the weights in the end
- Industry distribution of the portfolio

## Research questions to answer

- How good is the portfolio?
- Challenge - Does auto rebalance improve the performance?

## Datasets to be used

- Alpaca
- Yahoo Finance
- Monte Carlo
- Google Maps API (if there is any)

## Rough breakdown of tasks

Modules:

- User input UI - to use Javascript or Python ??? (need to check)
- API connection and data download (based on user input) - Stock price
- API connection and data download (based on user input) - Crypto price
- Data cleaning
- Monte Carlo analysis
- Dashboards to show
  - High Risk - high returns
  - edium risk
  - Low risk - low volatility

**Challenge:**

- API connection and data download (based on user input) - Stock lat/long and other relevant data
- Mapbox - show the stock location geographically. Make bubbles larger for larger weightings or larger returns
