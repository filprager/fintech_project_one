import panel as pn

def make_interface(plot1, plot2):
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