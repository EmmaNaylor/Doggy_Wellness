from application import db
from dataclasses import dataclass

@dataclass
class Activity(db.Model):
    id: int
    activity_name: str
    description: str
    activity_type: str
    supervision: str

    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    activity_type = db.Column(db.String(15), nullable=False)
    supervision = db.Column(db.String(15), nullable=True)

