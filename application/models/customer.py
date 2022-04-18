from application import db
from dataclasses import dataclass


@dataclass
class Customer(db.Model):
    id: int
    first_name: str
    last_name: str
    email: str
    telephone_number: str
    dog_name: str

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telephone_number = db.Column(db.String(12), nullable=True)
    dog_name = db.Column(db.String(25), nullable=False)
