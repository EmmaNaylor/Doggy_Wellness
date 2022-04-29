from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField, ValidationError
from wtforms.validators import InputRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email('Invalid email - missing @ character'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=100)])


