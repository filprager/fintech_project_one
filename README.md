# FinTech Project 1.0.0

## Project title

- Financial Analysis Tool - FAT (Delorean)
- My Portfolio

## Installation and APP Startup

### Python App

<u>Installations</u>
pip install datetime
pip unstall pytz
pip install python-dotenv
pip install alpaca-trade-api
pip install package_name
conda install panel
conda install panda
conda install numpy  
 conda install -c anaconda nb_conda -y
conda install -c conda-forge nodejs -y
conda install -c pyviz holoviz -y
conda install -c plotly plotly -y

<u>Start app by executing</u>
main.ipyd

<u>Files needed for the app</u>
main.ipyd
get_data.py
process_data.py
visualize_data.py
make_interface.py
MCForecastTools.py

### Flasks UI App

<u>Installation</u>
pip install flask
pip install flask_wtf
pip install wtforms
pip install wtforms.validators

<u>Start app by executing</u>
python flaskinput.py

<u>Files needed for the app</u>
flaskinput.py
ui_output.py
/assets
/templates

## OVERVIEW - WORKFLOW

1. create 1 portfolio (For now can expand later)
2. each portfolio has 1-5 stocks with manual weighting
3. Initial investment - default $1000
4. backward view - historical price chart per stock (overlayed view), and combined historical return/ cumulative return across all stocks
   _combined historical return/ cumulative return across all portfolios_
5. single forward view - Monte carlo on stocks
   _monte carlo projection for each portfoli ie: Portfolio1, Portfolio2, Portfolio3_
6. COMPARE - portfolio to the 4 main INDICES
7. Calculate and output projection of Total return and Average Annual Return for the inital investment

## Project description/outline

User inputs:

- Initial investment
- Max 5 stocks -> compute
  - Historical graph for each stock
  - joint graph of 5 stocks
- Initial weight of each ticker (incl. sum check)
- create portfolio (button)
- Start Date (date range)
- End Date (date range) : Default Today
- _Challenge - Enable/disable auto rebalance_
- _ADD crypto tickers _ API available

### Schema

portfolio_1{
ticker{
"MSFT" : 0.2,
"AAPL": 0.2,
"TSLA": 0.2,
"GOOG": 0.2,
"BRK": 0.2  
 },
date_range{
start_date: 11/12/2019,
end_data: 11/12/2020
}
}

### STOCK DATA:

- Alpaca
- S&P 500
- NASDAQ 100
- DOW JONES
- Russell 2000

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

- Make the interface for the app (main.ipynb, make_interface.py) - Raj
- Get the data via APIs (get_data.py) - Mark
- Process the data (process_data.py) - Ivan
- Visualize the data (visualize_data.py) - Fil
