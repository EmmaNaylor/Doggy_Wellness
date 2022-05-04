from application import db
from sqlalchemy import func
from application.models.activity import Activity
from application.models.event_info import Event
from application.models.booking import Booking
from application.models.customer import Customer


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
    return Event.query


def add_new_booking(new_customer, classbooking, dogbooked):
    new_customer.booking = []
    new_customer.booking.append(classbooking)
    new_customer.booking.append(dogbooked)
    db.session.add(new_customer)
    db.session.add(classbooking)
    db.session.add(dogbooked)
    db.session.commit()


def age_query():
    ages = ['0-3 years', '4-7 years', '8+ years']
    print(ages)
    return ages


def size_query():
    sizes = ['small', 'medium', 'large']
    print(sizes)
    return sizes


def temperament_query():
    temperament = ['couch potato', 'moderate', 'energetic']
    print(temperament)
    return temperament


def size_check(dog_size):
    if dog_size == "Small":
        amount = "30 minutes"
        return amount
    elif dog_size == "Medium":
        amount = "60 minutes"
        return amount
    elif dog_size == "Large":
        amount = "90 minutes"
        return amount


def fav_class(dog_energy):
    if dog_energy == "Couch Potato":
        recommendation = "Yoga"
        return recommendation
    elif dog_energy == "Moderate":
        recommendation = "Doggy Zumba"
        return recommendation
    elif dog_energy == "Active":
        recommendation = "Canine Circuit Training"
        return recommendation

def name(user):
    customer = db.session.query(Customer).filter(Customer.id == user).first()
    if not customer:
        return "Larry"
    return customer.first_name

def display_all_bookings():
    all_bookings = db.session.query(Customer, Booking, Event, Activity) \
        .select_from(Customer).join(Booking).join(Event).join(Activity).all()
    return all_bookings


def display_customer_bookings(user):
    customer_bookings = db.session.query(Customer, Booking, Event, Activity) \
        .select_from(Customer).join(Booking).join(Event).join(Activity).filter(Customer.id == user).all()
    return customer_bookings

    # def display_booking_summary():
    #     booking_summary = db.session.query(Customer, Booking, Event, Activity) \
    #         .select_from(Customer).join(Booking).join(Event).join(Activity).all()
    #     return booking_summary