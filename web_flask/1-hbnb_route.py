#!/usr/bin/python3

"""This is a root for the hbnb function"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    # run the app on 0.0.0.0:5000
    app.run(debug=True, port=5000, host="0.0.0.0")
