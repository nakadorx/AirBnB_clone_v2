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


@app.route('/hbnb_filters', strict_slashes=False)
def StatesAndcitiesByState():
    """StatesAndcitiesByState"""
    st = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=st, amenities=amenities)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
