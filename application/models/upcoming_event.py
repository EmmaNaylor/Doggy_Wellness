from application import db
from dataclasses import dataclass


@dataclass
class Booking(db.Model):
    id: int
    activity_id: int
    event_info: int

    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
    event_info = db.Column(db.Integer, db.ForeignKey("event_info.id"), nullable=False)
