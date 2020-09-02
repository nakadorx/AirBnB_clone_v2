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
    return "C %s" % text.replace('_', ' ')


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def pythonIsCool(text):
    """pyhton is cool
    """
    return "Python %s" % text.replace('_', ' ')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
