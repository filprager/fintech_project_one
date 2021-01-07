import panel as pn

def make_interface(plot1, plot2, plot3, plot4): #plot3, plot4
    
#     welcome_panel = pn.Column(
#     "# Welcome to DeLorean",
#     "### This financial analysis tool presents a visual analysis of historical stock ticker performance for a selected date range, as well as predicted future performance using Monte Carlo analysis",
#     "### You can navigate through the tabs above to explore more detail about your selected stock tickers"
#     )
    
#     tabs = pn.Tabs(
#         ("Welcome", welcome_panel),
#         ('Historical - Line', plot1),
#         ('Historical - Bar', plot2),
#         ('Projected - Monte Carlo', plot3),
#         ('Projected - Distribution', plot4)


    # Content for the Past Performance tab
    past_performance = pn.Column(plot1,
                                 plot2,
                                 '## More plots can be placed here')
    
    # Content for the Future Performance tab
    future_performance = pn.Column('## Monte Carlo simulation goes here')

    tabs = pn.Tabs(
        ('Past Performance', past_performance),
        ('Future Performance', future_performance)
    )
    
    return tabs