#!/usr/bin/python3

"""This module render the list of different states"""

from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def state_list():
    all_state = storage.all(State)
    state_list = {}

    for k, v in all_state.items():
        state_list[k] = v.__dict__

    # return state_list
    return render_template("7-states_list.html", all_state=state_list)


if __name__ == "__main__":
    # run the ap on 0.0.0.0:5000
    app.run(debug=True, port=5000, host="0.0.0.0")
