class News:
    '''
    News class to define Movie Objects
    '''

    def __init__(self,title,description,url,urlToImage,publishedAt,content):
        self.title = title
        self.description = description
        self.url= url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
