from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField

class SignUpForm(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    email = StringField('Email Address: ')
    telephone_number = StringField('Contact Tel: ')
    dog_name = StringField("Dog's name: ")
    sign_up = SubmitField('Sign Up')
