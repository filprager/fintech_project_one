# Import libraries

import hvplot.pandas
from MCForecastTools import MCSimulation
import json

# Create a function that generates a plot based on the given data
def make_plot1(df):
    plot1 = df.hvplot(title="Historical Cumulative Returns of individual tickers, portfolio and market (S&P500) - Line", xlabel="Date", ylabel="Cumulative Return", rot=90, width = 800, height = 400).opts(yformatter="%.0f")
    return plot1

def make_plot2(df):
    plot2 = df.hvplot.area(title="Historical Cumulative Returns of individual tickers, portfolio and market (S&P500) - Area", xlabel="Date", ylabel="Cumulative Return", rot=90, width = 800, height = 400).opts(yformatter="%.0f")
    return plot2

def make_plot3(df):
    plot3 = df.hvplot.bar(title="Historical Cumulative Returns of individual tickers, portfolio and market (S&P500) - Bar", xlabel="Date", ylabel="Cumulative Return", rot=90, width = 800, height = 400).opts(yformatter="%.0f")
    return plot3

def make_plot4(df):
    plot4 = df.hvplot(title="Monte Carlo Simulation of Cumulative Portfolio Returns over the next 10 years", xlabel="Date", ylabel="Cumulative Return", rot=90, width = 800, height = 600).opts(yformatter="%.0f")
    return plot4

def make_plot5(string):
    plot5 = string
    return plot5
