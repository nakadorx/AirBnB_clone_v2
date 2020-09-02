#!/usr/bin/python3
"""script
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    """[teardown method]
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def statesList():
    """[stateList method]
    Returns:
        [html]: [fetches html page]
    """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)