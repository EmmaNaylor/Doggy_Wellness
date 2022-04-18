from application import db
from dataclasses import dataclass


@dataclass
class Dog(db.Model):
    id: int
    dog_name: str
    breed: str
    age: int
    size: str
    energy_level: int
    temperament: int
    dog_owner: int

    id = db.Column(db.Integer, primary_key=True)
    dog_name = db.Column(db.String(40), nullable=False)
    breed = db.Column(db.String(40), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    size = db.Column(db.String(12), nullable=True)
    energy_level = db.Column(db.String(12), nullable=True)
    temperament = db.Column(db.Integer, db.ForeignKey("dog_category.id"), nullable=True)
    dog_owner = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)

