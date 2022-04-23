from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for
from wtforms.validators import input_required, email
from flask_wtf import FlaskForm
from os import getenv
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

js = Bundle('main.js', 'scrollreveal.min.js', output='gen/main.js')
assets.register('all_js', js)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/dog_wellness_service"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lc335UfAAAAAOqkJJi0K84_rA_ut9ddvWvGUWsH'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lc335UfAAAAAEDijAaaBQl9BKzCbRaLeRJ-ggG1'

db = SQLAlchemy(app)
