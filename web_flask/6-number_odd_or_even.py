#!/usr/bin/python3
"""script
"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display n
    """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    """html
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ htmlpage6"""
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
