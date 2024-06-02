#!/usr/bin/python3
""" My First Web app """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Return message on open """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display on route """
    return "HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
