# Import libraries
from panel.interact import interact, interact_manual
import panel as pn

# Import self-made modules
from get_data import get_data_stock, get_data_market
from process_data import process_data_cumulative_returns, process_data_monte_carlo
from visualize_data import make_plot1, make_plot2, make_plot3, make_plot4
from make_interface import make_interface
from MCForecastTools import MCSimulation

# Create a function to generate the app


def create_app():
    # Create a function to generate the app


def create_app(ticker1, weight1, ticker2, weight2, ticker3, weight3, ticker4, weight4, ticker5, weight5):
    # Put all valid tickers (i.e. not an empty string) into a list (tickers), and their associated weights into a another list (weights)
    # tickers = []
    # weights = []

    # if ticker1 != '':
    #     tickers.append(ticker1)
    #     weights.append(weight1)
    # if ticker2 != '':
    #     tickers.append(ticker2)
    #     weights.append(weight2)
    # if ticker3 != '':
    #     tickers.append(ticker3)
    #     weights.append(weight3)
    # if ticker4 != '':
    #     tickers.append(ticker4)
    #     weights.append(weight4)
    # if ticker5 != '':
    #     tickers.append(ticker5)
    #     weights.append(weight5)

    # # Check if the sum of all weights = 1
    # if sum(weights) != 1:
    #     return 'Make sure the sum of your weights is equal to 1'

    # # --------------------- Get the data from APIs ---------------------
    # # Get data for given stocks
    # raw_data_stock = get_data_stock(tickers)

    # # Get data of the market (i.e. S&P 500 index)
    # raw_data_market = get_data_market()

    # # --------------------- Process the data ---------------------
    # processed_data = process_data_cumulative_returns(raw_data_stock, tickers, weights, raw_data_market)
    # processed_data_monte_carlo = process_data_monte_carlo(raw_data_stock, weights)

    # # --------------------- Visualize the data ---------------------
    # plot1 = make_plot1(processed_data)
    # plot2 = make_plot2(processed_data)
    # plot3 = make_plot3(processed_data_monte_carlo)
    # plot4 = make_plot4(processed_data_monte_carlo)

    # # --------------------- Make the interface of the app ---------------------
    # app = make_interface(plot1, plot2, plot3, plot4)

    # print(type(app))

    # return app

    return 'my .py is working '
