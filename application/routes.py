import json
from flask import render_template, request, jsonify
# import service
from application import app

@app.route('/', methods=['GET'])
def hello():
    return render_template("home.html", title="Home")
