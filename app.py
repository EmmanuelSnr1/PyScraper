# Import the flask module. An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, jsonify
import pprint
from scraper import * # import the function
import requests as request 



# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call the associated function.
@app.route('/')
# ‘/’ URL is bound with welcome() function.
def welcome():
    return render_template('index.html')

@app.route('/scrape_yahoo')
def scrape_yahoo():
    url = 'https://uk.finance.yahoo.com/'
    news = scrape_website(url, 'a', 'class', 'Fw(b)')  # use the function here
    print("The news are:")
    pprint.pprint(news)
    return render_template('scrape.html', news=news)  # render the template and pass the data

@app.route('/scrape_another_site')
def scrape_another_site():
    url = 'https://www.bbc.co.uk/news'
    # Here you would specify the tag and (optional) class that contain the article titles on this other site:
    news = scrape_website(url, 'tag', 'attr_type', 'attr_value')
    return render_template('scrape.html', news=news)


@app.route('/scrape')
def scrape():
    url = 'https://metro.co.uk/news/'
    # Here you would specify the tag and (optional) class that contain the article titles on this other site:
    content = scrape_site(url)
    return render_template('scrape.html', content=content)



# @app.route('/chat', methods=['POST'])
# def chat():
#     message = request.json['message']
#     response = run_chat(message)

#     return jsonify({'response': response})

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
     app.run(debug=True)
