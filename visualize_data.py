# Import libraries

import hvplot.pandas
from MCForecastTools import MCSimulation
import json

# Create functions that generate a plot based on the given data - Past Performance

def make_plot1(df):
    plot1 = df.hvplot(title="Historical Cumulative Returns of Individual Tickers, Portfolio and Market (S&P500) - Line", xlabel="Date", ylabel="Cumulative Return", rot=90, width = 800, height = 400, shared_axes=False).opts(yformatter="%.1f")
    return plot1

def make_plot2(df):
    plot2 = df.hvplot.area(title="Historical Cumulative Returns of Individual Tickers, Portfolio and Market (S&P500) - Stacked Area", xlabel="Date", ylabel="Cumulative Return", rot=90, width = 800, height = 400, shared_axes=False).opts(yformatter="%.1f")
    return plot2

def make_plot3(df):
    plot3 = df.hvplot.bar(title="Historical Cumulative Returns of Individual Tickers, Portfolio and Market (S&P500) - Bar", xlabel="Date", ylabel="Cumulative Return", rot=90, width = 800, height = 400, shared_axes=False).opts(yformatter="%.1f")
    return plot3

def make_plot4(df):
    plot4 = df.hvplot(title="Historical Daily Returns of Individual Tickers", xlabel="Date", ylabel="Daily Return", rot=90, width = 800, height = 400, shared_axes=False).opts(yformatter="%.2f")
    return plot4


# Create functions that generate a plot based on the given data - Future Performance

def make_plot5(df):
    plot5 = df.hvplot(title="Monte Carlo Simulation of Cumulative Portfolio Returns over the next 10 years", xlabel="Trading Days", ylabel="Cumulative Return", rot=90, width = 800, height = 600, shared_axes=False).opts(yformatter="%.0f")
    return plot5

def make_plot6(string):
    plot6 = string
    return plot6


# Create functions that generate a plot based on the given data - Risk Analysis

def make_plot7(df):
    plot7 = df.hvplot.box(title="Box Plot of Daily Returns of Individual Tickers", width=800, height=400, legend=False, shared_axes=False).opts(yformatter="%.2f")
    return plot7

def make_plot8(df):
    plot8 = df.hvplot(title="Rolling Standard Deviation of Individual Tickers - 21 Day Window", xlabel="Date", ylabel="Standard Deviation", rot=90, width = 800, height = 400, shared_axes=False).opts(yformatter="%.2f")
    return plot8

def make_plot9(df):
    plot9 = df.hvplot.heatmap(title="Ticker Correlation", width = 800, height = 400, shared_axes=False)
    return plot9