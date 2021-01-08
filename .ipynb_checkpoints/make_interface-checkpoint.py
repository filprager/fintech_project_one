import panel as pn
from MCForecastTools import MCSimulation
import json

def make_interface(plot1, plot2, plot3, plot4, plot5, plot6, plot7, plot8, plot9): 
    
    # Content for the Past Performance tab
    past_performance = pn.Column(
        plot1,
        plot2,
        plot3,
        plot4
    )
    
    # Content for the Future Performance tab
    future_performance = pn.Column(
        plot5, 
        plot6
    )
    
      # Content for the Risk Analysis tab
    risk_analysis = pn.Column(
        plot7, 
        plot8,
        plot9
    )

    tabs = pn.Tabs(
        ('Past Performance', past_performance),
        ('Future Performance', future_performance),
        ('Risk Analysis', risk_analysis)
    )
    
    return tabs