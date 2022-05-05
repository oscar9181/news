
from flask import render_template,redirect,url_for
from app import app
from .request import get_news,search_news



# Views
@app.route('/')
def index():    
    '''
    View root page function that returns the index page and its data
    '''
    #getting news
    
    sports_news =get_news('sports')
    politics_news = get_news('politics')
    business_news = get_news('business')
    title = 'Welcome to todays Bulletin'
 
    return render_template('index.html',title=title,sports =sports_news,politics =politics_news,business=business_news)


@app.route('/news/<int:id>')
def news(news_id):

    '''
    View source page function that returns the movie details page and its data
    '''
    
    

    return render_template('news.html',id=news_id)

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)




    