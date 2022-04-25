from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import InputRequired, email
from wtforms_sqlalchemy.fields import QuerySelectField
from application.models import activity
from application.service import activity_name_query, event_query


class bookingForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[InputRequired("Please enter your first name")])
    last_name = StringField('Last Name: ', validators=[InputRequired("Please enter your last name")])
    email = StringField('Email Address: ', validators=[InputRequired("An email address is required")])
    telephone_number = StringField('Contact Tel: ', validators=[InputRequired("A telephone number is required")])
    dog_name = StringField("Dog's name: '", validators=[InputRequired("Please enter your dog's name")])
    activity = QuerySelectField(query_factory=activity_name_query, allow_blank=False, get_label='activity_name')
    event = QuerySelectField(query_factory=event_query, allow_blank=False, get_label='event_date')
    recaptcha = RecaptchaField()
    book_class = SubmitField('Book Class')



