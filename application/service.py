from application import db
from application.models.activity import Activity

def activities():
    return Activity.query.all()
