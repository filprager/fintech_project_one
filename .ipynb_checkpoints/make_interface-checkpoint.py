import panel as pn

def make_interface(plot1, plot2):
    # Content for the Past Performance tab
    past_performance = pn.Colu
    
    tabs = pn.Tabs(
        ('Past Performance', plot1),
        ('Future Performance', plot2)
    )
    
    return tabs