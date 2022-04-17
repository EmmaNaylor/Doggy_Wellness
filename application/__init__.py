from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/dog_wellness_service"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

db = SQLAlchemy(app)
