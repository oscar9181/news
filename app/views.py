from flask import render_template
from app import app
from .request import get_news


# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    business_news =get_news('business')
    sports_news=get_news('sports')
    politics_news=get_news('politics')
    title = 'Bulletin- Welcome to todays news'
    
    return render_template('index.html', title = title,business = business_news,sports =sports_news,politics =politics_news)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''

    return render_template('news.html',id=news_id)
