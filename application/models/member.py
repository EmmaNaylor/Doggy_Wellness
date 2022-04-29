from application import db
from application import Login_Manager
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

@dataclass
class Member(UserMixin, db.Model):
    id: int
    email: str
    user_password: str
    linked_customer: int

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    user_password = db.Column(db.String(80))
    linked_customer = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)

@Login_Manager.user_loader
def load_user(id):
    return Member.query.get(int(id))
