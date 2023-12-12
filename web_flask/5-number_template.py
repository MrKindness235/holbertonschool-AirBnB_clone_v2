#!/usr/bin/python3
"""
This is a major update to 0.
It also displays hbnb.
Added print_C function.
Added the print_python function.
Added the print_number function; this one is interesting
since it has an "only if int" condition.
Both listen to 0.0.0.0, port 5000.
"""


from flask import Flask
from flask import render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def print_number(n):
    """Function that displays 'n is a number', only if n is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def print_number(n):
    """Function that renders 5-number.html only if n is an integer."""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
