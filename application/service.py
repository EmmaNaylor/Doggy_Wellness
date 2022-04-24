from application import db
from application.models.activity import Activity
from application.models.event_info import Event


def activities():
    return Activity.query.all()


def add_new_customer(customer, dog):
    db.session.add(customer, dog)
    db.session.commit()


def activity_name_query():
    return Activity.query


def event_query():
    return Event.query


def add_new_booking(classbooking):
    db.session.add(classbooking)
    db.session.commit()

    # id = db.Column(db.Integer, primary_key=True)
    # customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    # activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
    # event_id = db.Column(db.Integer, db.ForeignKey("event_info.id"), nullable=False)
    # dog_name = db.Column(db.String(40), nullable=True)
