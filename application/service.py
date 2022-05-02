from sqlalchemy import func

from application import db
from application.models.activity import Activity
from application.models.booking import Booking
from application.models.customer import Customer
from application.models.event_info import Event


def activities():
    return Activity.query.all()


def add_new_customer(customer):
    db.session.add(customer)
    db.session.commit()


def add_new_member(new_member):
    db.session.add(new_member)
    db.session.commit()


def activity_name_query():
    print(Activity.query)
    return Activity.query


def event_query():
    print(Event.query)
    return Event.query.all


def add_new_booking(new_customer, classbooking, dogbooked):
    new_customer.booking = []
    new_customer.booking.append(classbooking)
    new_customer.booking.append(dogbooked)
    db.session.add(new_customer)
    db.session.add(classbooking)
    db.session.add(dogbooked)
    db.session.commit()


def display_all_bookings():
    all_bookings = db.session.query(Customer, Booking, Event, Activity) \
        .select_from(Customer).join(Booking).join(Event).join(Activity).all()

    return all_bookings


def display_customer_bookings():
    customer_bookings = db.session.query(Customer, Booking, Event, Activity) \
        .select_from(Customer).join(Booking).join(Event).join(Activity).filter(Customer.id == 1).all()
    return customer_bookings


# def display_booking_summary():
#     booking_summary = db.session.query(Customer, Booking, Event, Activity) \
#         .select_from(Customer).join(Booking).join(Event).join(Activity).all()
#     return booking_summary


