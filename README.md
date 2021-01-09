# FinTech Project 1.0.0

## Project title

- Financial Analysis Tool - FAT (Delorean)
- My Portfolio

## Installation and APP Startup

### Python App

#### Installations

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

#### Start app by executing

main.ipyd

#### Files needed for the app

main.ipyd
get_data.py
process_data.py
visualize_data.py
make_interface.py
MCForecastTools.py

### Flasks UI App

#### Installation

pip install flask
pip install flask_wtf
pip install wtforms
pip install wtforms.validators

#### Start app by executing

python flaskinput.py

#### Files needed for the app

flaskinput.py
ui_output.py
/assets
/templates

## OVERVIEW - WORKFLOW

1. Select Start Date
2. Select End Date
3. each portfolio has 1-5 stocks with manual weighting
4. Initial investment - default $1000
5. Run Interact Button
6. Output Past Performance - historical price chart per stock (overlayed view), and combined historical return/ cumulative return across all stocks
   _combined historical return/ cumulative return across all portfolios_
7. Output future Performance - Monte carlo on stocks
   _monte carlo projection for each stock_
8. Output Risk Analysis

## Project description/outline

User inputs:

- Initial investment
- Max 5 stocks -> compute
  - Historical graph for each stock
  - joint graph of 5 stocks
- Initial weight of each ticker (incl. sum check)
- Run Interact (button)
- Start Date (date range)
- End Date (date range) : Default Today

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

## Datasets to be used

- Alpaca
- Yahoo Finance
- Monte Carlo

## APP Output

in a TAB Layout

- Past performance of the selected stocks - Daily Returns, Cumulative Returns
- Future performance of the selected stocks - using monte Carlo, Cumulative returns
- Risk Analysis - Box Plot, Correlation graph, Rolling Std of Daily Returns

## NEXT Step

1. Refine ticker cound and weights
2. Migrate to a NEW API
3. Update Monte Carlo py
4. Create and compare multiple custom portfolios
5. Intergration with exchanges to offer 'Buy Now' functionality
6. Improved GUI for Web and Mobile - hooking up the Front-End UI to Python for processing.
