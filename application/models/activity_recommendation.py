from application import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

@dataclass
class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dog_category = db.Column(db.Integer, db.ForeignKey("dog.category.id"), nullable=False)
    activity_recommendation = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
