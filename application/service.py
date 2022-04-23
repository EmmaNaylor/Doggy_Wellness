from application import db
from application.models.activity import Activity


def activities():
    return Activity.query.all()


def add_new_customer(customer, dog):
    db.session.add(customer, dog)
    db.session.commit()
