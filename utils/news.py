from dash import Dash, html, dcc
from GoogleNews import GoogleNews

class bballNews():
    
    def __init__(self):
        self.newsArticles = self.getTop10News(1)
        
    def getTop10News(self, page):
        googlenews = GoogleNews()
        googlenews.search('UVA Basketball')
        news = googlenews.results(sort=True)
        news = [[article['title'], article['media'], article['link']] for article in news]
        return news
        
    def construct_news_pane(self):
        return html.Div([
                    html.H3("Recent News", style={'textAlign': 'center'}),
                    html.Ul(id='news-list', children=[
                        html.Li([html.A(i[0], href=i[2], target="_blank"), html.Br(), html.Small(html.I(i[1]))]) for i in self.newsArticles
                    ])
                ])