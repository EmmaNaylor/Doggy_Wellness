from application import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@dataclass
class Event(db.Model):
    __tablename__ = 'event_info'
    id: int
    activity_id: int
    event_date: str
    start_time: str
    end_time: str
    duration: str
    cost: int
    capacity: int
    location: str

    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
    event_date = db.Column(db.String(8), nullable=False)
    start_time = db.Column(db.String(8), nullable=False)
    end_time = db.Column(db.String(8), nullable=True)
    duration = db.Column(db.String(8), nullable=True)
    cost = db.Column(db.Integer, nullable=True)
    capacity = db.Column(db.Integer, nullable=True)
    location = db.Column(db.String(15), nullable=True)
    booking_info = db.relationship("Booking", backref='event_info')

    def __repr__(self):
        return '{}'.format(self.id)
