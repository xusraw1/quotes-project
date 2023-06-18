from flask import Flask, render_template
from key import KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY


@app.route('/')
def main():

    return render_template('index.html')

