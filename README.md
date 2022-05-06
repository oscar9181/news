 # Vidokezo
 # Author:Oscar Okola
 # Description
 This is a flask application page that contains news articles from different sources where a user can be able access latest updates in the world today.

 # User Interaction
 # As a user:
   - I would want to see the news images.
   - I would want to see the news article
   - I would want to visit and open links to other pages
   - I would want to see different  categories of news sources

 # BDD
 | Behaviour               |  Input        |   Output                         |
 | :-----------:           |:-----:        | :-------------:                  | 
   Display news with        On page load     News is displayed in homepage    
 |  categories             |               |                                  |
 |                         |               |                                  |
   Display artcles from       click  a news  Redirected to a page with article 
 | news source             |  source link  |   sources                        |

 
 
 ## Basics
 # Creating and activating virtual environment
    $ python3.9 -m venv --without-pip virtual
    $ source virtual/bin/env

 ## Setting up Apllication
    $ Python3.9
    $ pip install flask
    $ virtual env
    
 #### Adding modules
  $ python3.9 -m pip install Flask-Bootstrap
  
  ### Getting News_Api key
  #### In order your page to contain news article you should have an api key:
   - Visit https://newsapi.org/ to generate your api key
   - Create a file in the root directory 
   - Insert the  news api key
    
  ## Technologies Used
   - Python 3.9
   - Flask

 ## Contributions
 You can fork the repository create your own branch on the terminal you git add then commit and finally push changes lastly
 you pull request for the author to access the code.
 
 ## License
 MIT License

Copyright (c) [2022] [Oscar Okola]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
