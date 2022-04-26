from application import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@dataclass
class Booking(db.Model):
    __tablename__ = 'user_booking'
    id: int
    customer_id: int
    activity_id: int
    event_id: int
    dog_name: str

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("event_info.id"), nullable=False)
    dog_name = db.Column(db.String(40), nullable=True)

