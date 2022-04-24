from application import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

@dataclass
class RedundantBooking(db.Model):
    id: int

    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
    event_info = db.Column(db.Integer, db.ForeignKey("event_info.id"), nullable=False)
