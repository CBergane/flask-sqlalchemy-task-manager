from flask import render_template

from taskmanager import app, db  # type: ignore


@app.route("/")
def home():
    return render_template("base.html")
