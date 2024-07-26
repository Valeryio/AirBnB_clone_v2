#!/usr/bin/python3

"""This module creates a minimal web application in Flask"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "<p>Hello HBNB!</p>"

if __name__ == "__main__":
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000, host="0.0.0.0")
