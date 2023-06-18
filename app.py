from flask import Flask, render_template
from key import KEY
import requests

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


if __name__ == '__main__':
    app.run(debug=True)
