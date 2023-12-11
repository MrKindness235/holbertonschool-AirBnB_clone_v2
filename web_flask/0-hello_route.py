#!/usr/bin/python3
"""
This code creates an intance of Flask and makes
it listen to 0.0.0.0, port 5000.
It returns "Hello HBNB!" as display.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Main function"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
