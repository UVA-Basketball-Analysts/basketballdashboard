from dash import Dash, html, dcc

class bballNews():
    
    def __init__(self):
        self.newsArticles = [
            ['Louisville Cardinals lose to No. 7 Virginia Cavaliers in home ACC college basketball game', 'https://www.courier-journal.com/story/sports/college/louisville/2023/02/15/louisville-basketball-vs-uva-how-to-watch-stream-and-live-updates/69863328007/'],
            ['Virginia Avoids Disastrous Upset, Escapes Louisville With Sloppy 61-58 Win', 'https://www.si.com/college/virginia/basketball/virginia-avoids-disastrous-upset-escapes-louisville-with-sloppy-61-58-win'],
            ['Franklin, Clark help No. 7 UVA outlast ACC-worst Louisville', 'https://www.espn.com/mens-college-basketball/recap/_/gameId/401488496']
        ]
        
        self.markdown_text = '''
            ### Header of Markdown
            From newsObject

        '''
        
    def construct_news_pane(self):
        return html.Div([
                    html.H3("Recent News", style={'textAlign': 'center'}),
                    html.Ul(id='news-list', children=[
                        html.Li(html.A(i[0], href=i[1], target="_blank")) for i in self.newsArticles
                    ]),
                dcc.Markdown(children = self.markdown_text)
                ])