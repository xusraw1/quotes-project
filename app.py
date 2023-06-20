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
    ## Завтро не забудь добавить еще вторую страницу!!!
    page = random.randint(1, 50)
    response1 = requests.get(f"https://api.quotable.io/quotes?page={page}").json()['results']

    list = random.sample(response1, k=10)
    quotes = {
        'quotes': list
    }
    return render_template('quotes_list.html', quotes=quotes['quotes'])


@app.route('/<auth>/quotes')
def author(auth):
    response = requests.get(f"https://api.quotable.io/quotes?author={auth}").json()['results']
    list = random.choice(response)

    return render_template("author.html", quote=list)


@app.route('/short_quote')
def short_quote():
    response = requests.get("https://api.quotable.io/quotes/random?maxLength=50").json()
    return render_template("short.html", quote=response[0])


if __name__ == '__main__':
    app.run(debug=True)
