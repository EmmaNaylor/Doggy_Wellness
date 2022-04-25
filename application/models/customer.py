from application import db
from dataclasses import dataclass
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@dataclass
class Customer(db.Model):
    id: int
    first_name: str
    last_name: str
    email: str
    telephone_number: str

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telephone_number = db.Column(db.String(12), nullable=True)

    # dogs = db.relationship("Dog", backref="customer")


# Customer.dogs = relationship("Dogs", back_populates="customer")
