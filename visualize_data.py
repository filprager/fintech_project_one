# Import libraries
import hvplot.pandas

# Create a function that generates a plot based on the given data
def make_plot1(df):
    plot1 = df.hvplot()
    return plot1

def make_plot2(df):
    plot2 = df.hvplot.area()
    return plot2