# Import libraries
from panel.interact import interact

# Import self-made modules
from get_data import get_data_stock, get_data_market
from process_data import process_data
from visualize_data import make_plot1, make_plot2
from make_interface import make_interface

# Create a function to generate the app


def create_app():
    print('create_app get it working')
    # Check if the sum of all weights = 1
    if weight1 + weight2 != 1:
        return 'Make sure the sum of your weights is 1'

    # --------------------- Get the data from APIs ---------------------
    # Get data for given stocks
    tickers = [ticker1, ticker2]
    raw_data_stock = get_data_stock(tickers)

    # Get data of the market (i.e. S&P 500 index)
    raw_data_market = get_data_market()

    # --------------------- Process the data ---------------------
    tickers = [ticker1, ticker2]
    weights = [weight1, weight2]
    processed_data_stock = process_data(raw_data_stock, tickers, weights)

    # --------------------- Visualize the data ---------------------
    plot1 = make_plot1(processed_data_stock)
    plot2 = make_plot2(processed_data_stock)

    # --------------------- Make the interface of the app ---------------------
    app = make_interface(plot1, plot2)

    return app

    # return 'my .py is working '
