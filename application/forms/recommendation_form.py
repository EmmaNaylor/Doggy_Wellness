from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, IntegerField, PasswordField, SelectField
from wtforms.validators import InputRequired, email
from wtforms_sqlalchemy.fields import QuerySelectField

from application.models import activity
from application.service import activity_name_query, event_query, age_query, size_query, temperament_query


class Recommendation_Form(FlaskForm):
    dog_name = StringField('Name of Dog: ', validators=[InputRequired("Please enter your dogs name")])
    breed = StringField('Breed: ', validators=[InputRequired("Please enter your dogs breed")])
    age = SelectField('Age: ', choices=[('0-3 years', '0-3 years'), ('4-7 years', '4-7 years'), ('8+ years', '8+ years')])
    size = SelectField('Size: ', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    temperament = SelectField('Temperament: ', choices=[('Couch Potato', 'Couch Potato'), ('Moderate', 'Moderate'), ('Active', 'Active')])
    find_recommendations = SubmitField('Go')