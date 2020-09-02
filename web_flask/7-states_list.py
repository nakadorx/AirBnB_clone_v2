#!/usr/bin/python3
"""script
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    """teardown
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def statesList():
    """statesList
    """
    st = storage.all("State")
    return render_template('7-states_list.html', states=st)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
