import panel as pn

def make_interface(plot1, plot2, plot3, plot4):
    
    welcome_panel = pn.Column(
    "# Welcome to DeLorean",
    "### This financial analysis tool presents a visual analysis of historical stock ticker performance for a selected date range, as well as predicted future performance using Monte Carlo analysis",
    "### You can navigate through the tabs above to explore more detail about your selected stock tickers"
    )
    
    tabs = pn.Tabs(
        ("Welcome", welcome_panel),
        ('Historical - Line', plot1),
        ('Historical - Bar', plot2),
        ('Projected - Monte Carlo', plot3),
        ('Projected - Distribution', plot4)
    
    )
    
    return tabs