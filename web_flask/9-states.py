#!/usr/bin/python3
"""script
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    """teardown"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def StatesAndcitiesByState(id=None):
    """StatesAndcitiesByState"""
    st = storage.all("State")
    if id is None:
        return render_template('9-states.html', states=st)

    for st in storage.all("State").values():
        if st.id == id:
            return render_template("9-states.html", state=st)

    return render_template("9-states.html")


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
