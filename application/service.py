from application import db
from application.models.activity import Activity
from application.models.event_info import Event


def activities():
    return Activity.query.all()


def add_new_customer(customer):
    db.session.add(customer)
    db.session.commit()

def activity_name_query():
    print(Activity.query)
    return Activity.query


def event_query():
    print(Event.query)
    return Event.query


def add_new_booking(customer, classbooking):
    customer.booking = []
    customer.booking.append(classbooking)
    db.session.add(customer)
    # db.session.add(classbooking)
    db.session.commit()

    # id = db.Column(db.Integer, primary_key=True)
    # customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    # activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
    # event_id = db.Column(db.Integer, db.ForeignKey("event_info.id"), nullable=False)
    # dog_name = db.Column(db.String(40), nullable=True)
