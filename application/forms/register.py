from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(min=8, max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=100)])