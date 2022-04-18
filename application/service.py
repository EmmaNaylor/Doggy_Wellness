from application import db
from application.models.activity import Activity


def activities():
    return Activity.query.all()


def add_new_customer(customer):
    db.session.add(customer)
    db.session.commit()
