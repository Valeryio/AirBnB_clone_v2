#!/usr/bin/python3

"""This flask application display an app with a parameter"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


if __name__ == "__main__":
    # run the app on 0.0.0.0:5000
    app.run(debug=True, port=5000, host="0.0.0.0")
