from application import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@dataclass
class Activity(db.Model):
    __tablename__ = 'activity'
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
    bookings = db.relationship('Booking', backref='booking_id')

    def __repr__(self):
        return '[Choice {}]'.format(self.activity_name)
