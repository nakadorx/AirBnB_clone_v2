#!/usr/bin/python3
"""script
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    """despla hello hbnb
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """display hbnb
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ccc
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
