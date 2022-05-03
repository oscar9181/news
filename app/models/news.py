class News:
    '''
    News class to define Movie Objects
    '''

    def __init__(self,id,title,description,url,urlToImage,datepublished,content):
        self.id =id
        self.title = title
        self.description = description
        self.url= url
        self.urlToImage = urlToImage
        self.datepublished = datepublished
        self.content = content
