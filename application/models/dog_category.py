from application import db
from dataclasses import dataclass


@dataclass
class Category(db.Model):
    id: int
    size: str
    energy_level: str

    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(12), nullable=False)
    energy_level = db.Column(db.String(30), nullable=False)
