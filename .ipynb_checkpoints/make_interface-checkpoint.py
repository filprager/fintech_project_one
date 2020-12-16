import panel as pn

def make_interface(plot1, plot2):
    tabs = pn.Tabs(
        ('Tab1', plot1),
        ('Tab2', plot2)
    
    )
    
    return tabs