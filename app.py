from flask import Flask, render_template
from key import KEY
import requests
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY


@app.route('/')
def main():
    response = requests.get("https://api.quotable.io/quotes/random").json()
    context = {
        'author': response[0]['author'],
        'content': response[0]['content'],
    }
    return render_template('index.html', context=context)


@app.route('/quotes-list')
def quotes():
    response = requests.get("https://api.quotable.io/quotes?page=1").json()['results']
    list = random.sample(response, k=5)
    quotes = {
        'quotes': list
    }
    return render_template('quotes_list.html', quotes=quotes['quotes'])


if __name__ == '__main__':
    app.run(debug=True)
