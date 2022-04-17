import json
from flask import render_template, request, jsonify
from application import service
from application import app


@app.route('/', methods=['GET'])
def hello():
    return render_template("home.html", title="Home")


@app.route('/activity', methods=['GET'])
def show_activities():
    error = ""
    details = service.activities()
    if len(details) == 0:
        error = "There are no books to display"
    return render_template('test.html', activities=details, message=error)

