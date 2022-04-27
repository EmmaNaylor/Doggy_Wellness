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


def add_new_booking(new_customer, classbooking, dogbooked):
    new_customer.booking = []
    new_customer.booking.append(classbooking)
    new_customer.booking.append(dogbooked)
    db.session.add(new_customer)
    db.session.add(classbooking)
    db.session.add(dogbooked)
    db.session.commit()


