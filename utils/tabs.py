from dash import dcc
from dash import html


class BballTabs():
    def __init__(self):
        self.tabs_styles = {
            'height': '44px'
        }
        
        self.tab_style = {
            'borderBottom': '1px solid #d6d6d6',
            'padding': '6px',
            'fontWeight': 'bold'
        }

        self.tab_selected_style = {
            'borderTop': '1px solid #d6d6d6',
            'borderBottom': '1px solid #d6d6d6',
            'backgroundColor': '#119DFF',
            'color': 'white',
            'padding': '6px'
        }
        
    def hello(self):
        return 'hi'
    
    def constructTabs(self, num_of_tabs):
        return dcc.Tabs(\
            id='tabs-inline',\
            value='tab-1',\
            children = [dcc.Tab(label='Tab ' + str(i),\
                                value = 'tab-'+str(i),\
                                style=self.tab_style,\
                                selected_style=self.tab_selected_style) for i in range(1,num_of_tabs + 1)],\
                        style=self.tabs_styles \
            ),html.Div(id='tabs-content-inline-3')