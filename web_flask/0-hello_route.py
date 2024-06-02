#!/usr/bin/python3
""" My First Web app """
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ Return message on open """
    return "<p>Hello HBNB!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
