from application import db
from dataclasses import dataclass


@dataclass
class Recommendation(db.Model):
    id: int
    dog_category: int
    activity_recommendation: int

    id = db.Column(db.Integer, primary_key=True)
    dog_category = db.Column(db.Integer, db.ForeignKey("dog.category.id"), nullable=False)
    activity_recommendation = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
