#!/usr/bin/python3
""" My First Web app """
from flask import Flask, abort
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Return message on open """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display on route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def msg_c(text):
    """Display a message"""
    text = escape(text)
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def msg_py(text):
    """ Display a message """
    text = escape(text)
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<n>', strict_slashes=False)
def msg_num(n):
    """ Display a number """
    n = escape(n)
    try:
        n = int(n)
        return f'{n} is a number'
    except Exception:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
