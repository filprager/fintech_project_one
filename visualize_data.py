# Import libraries

import hvplot.pandas
from MCForecastTools import MCSimulation
import json

# Create a function that generates a plot based on the given data
def make_plot1(df):
    plot1 = df.hvplot()
    return plot1

def make_plot2(df):
    plot2 = df.hvplot.bar()
    return plot2

def make_plot3(df):
    plot3 = df.plot_simulation()
    return plot3

def make_plot4(df):
    plot4 = df.plot_distribution()
    return plot4