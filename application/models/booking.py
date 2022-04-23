from application import db
from dataclasses import dataclass


@dataclass
class Booking(db.Model):
    id: int

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    dog_id = db.Column(db.Integer, db.ForeignKey("dog.id"), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
    event = db.Column(db.Integer, db.ForeignKey("event_info.id"), nullable=False)
