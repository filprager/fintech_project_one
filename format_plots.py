import panel as pn

def format_plots(plot1, plot2):
    tabs = pn.Tabs(
        ('Tab1', plot1),
        ('Tab2', plot2)
    
    )
    
    return tabs