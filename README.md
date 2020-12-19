# FinTech Project 1

## Project title

- Investor Analysis Tool (‘sleek name here’)
- My Portfolio

## OVERVIEW - WORKFLOW
1. create 1 portfolio (For now can expand later)
2. each portfolio has 1-5 stocks with manual weighting
3. Initial investment - default $1000
3. backward view - historical price chart per stock (overlayed view), and combined historical return/ cumulative return across all stocks
   *combined historical return/ cumulative return across all portfolios*
4. single forward view - Monte carlo on stocks
   *monte carlo projection for each portfoli ie: Portfolio1, Portfolio2, Portfolio3*
5. Calculate and output projection of Total return and Average Annual Return for the inital investment


## Project description/outline

User inputs:
- create portfolio (button)
- Max 5 stocks -> compute
  - Historical graph for each stock
  - joint graph of 5 stocks

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

## Work distribution
- Make the interface for the app - Raj
- Get the data via APIs - Mark
- Process the data
- Visualize the data
