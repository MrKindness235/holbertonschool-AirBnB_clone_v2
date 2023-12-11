#!/usr/bin/python3
"""
This is a major update to 0.
It also displays hbnb.
Added print_C function.
Both listen to 0.0.0.0, port 5000.
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Hello function that displays:"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """Function that displays:"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def print_C(text):
    """Function that displays:"""
    return "C {}".format(escape(text).replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_python(text='is cool'):
    """Function that displays:"""
    return "Python {}".format(escape(text).replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
