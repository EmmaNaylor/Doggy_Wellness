from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import InputRequired, email


class SignUpForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[InputRequired("Please enter your first name")])
    last_name = StringField('Last Name: ', validators=[InputRequired("Please enter your last name")])
    email = StringField('Email Address: ', validators=[InputRequired("An email address is required")])
    telephone_number = StringField('Contact Tel: ', validators=[InputRequired("A telephone number is required")])
    # dog_name = StringField("Dog's name: '", validators=[InputRequired("Please enter your dog's name")])
    recaptcha = RecaptchaField()
    sign_up = SubmitField('Sign Up')
