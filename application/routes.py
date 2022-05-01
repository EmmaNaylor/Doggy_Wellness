import json
import mysql.connector
import pymysql
from flask_wtf import FlaskForm
from flask import render_template, request, jsonify, escape, url_for, redirect
from application import service
from application import app
from application.forms.signUp import SignUpForm
from application.forms.booking import bookingForm
from application.models.activity import Activity
from application.models.customer import Customer
from application.models.dog import Dog
from application.models.member import Member
from application.models.booking import Booking
from application.forms.recommendation_form import recommendation_form
from application.models.event_info import Event
from application.forms.login import LoginForm
from application.forms.register import RegisterForm
from flask_bootstrap import Bootstrap
from wtforms_sqlalchemy.fields import QuerySelectField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from email_validator import validate_email, EmailNotValidError


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.form)
        email = form.email.data
        user_password = form.password.data
        if form.validate_on_submit():
            member = Member.query.filter_by(email=form.email.data).first()
            if member:
                if check_password_hash(member.user_password, form.password.data):
                    login_user(member)
                    return redirect(url_for('dashboard'))
            return "Invalid username or password"
    return render_template('login', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.form)
        email = form.email.data
        user_password = form.password.data
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_member = Member(email=email, user_password=hashed_password)
            member_check = Member.query.filter_by(email=form.email.data).first()
            if member_check:
                return "Email is already in use"
            service.add_new_member(new_member)
            return redirect(url_for('dashboard'))
    return render_template('signup', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard', title="Dashboard", user=current_user.email)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

#@app.route('/recommendations', methods=['GET'])
#def recommendations():
    #return render_template("recommendations.html", title="Recommendations")


@app.route('/activity', methods=['GET'])
def show_activities():
    error = ""
    details = service.activities()
    if len(details) == 0:
        error = "There are no activities to display"
    return render_template('test.html', activities=details)


@app.route("/recommend")
def recommend():
    size = (request.args.get("size", ""))
    if size:
        answer = give_recommendation(size)
    else:
        answer = ""
    return (
            """<form action="" method="get">
              <input type="text" name="size" />
              <input type="submit" value="Give me a recommendation">
              </form>"""
            + "You should exercise your dog: "
            + answer
    )


@app.route("/recommendation", methods=['GET', 'POST'])
def give_recommendation():
    conn = pymysql.connect(host='localhost', user='root', passwd='password', db='dog_wellness_service')
    cursor = conn.cursor()
    cursor.execute('SELECT size FROM dog_category')
    sizelist = cursor.fetchall()
    return render_template('testing2.html', sizelist=sizelist)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = SignUpForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            return "Thanks! You're signed up!"
        form = SignUpForm(request.form)
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        telephone_number = form.telephone_number.data
        recaptcha = form.recaptcha
        customer = Customer(first_name=first_name, last_name=last_name, email=email, telephone_number=telephone_number)
        service.add_new_customer(customer)
    return render_template('index', form=form, title="Home")


@app.route('/classes', methods=['GET', 'POST'])
def booking():
    form = bookingForm()
    if request.method == 'POST':
            form = bookingForm()
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            telephone_number = form.telephone_number.data
            recaptcha = form.recaptcha
            dog_name = form.dog_name.data
            form.activity.query = Activity.query
            form.event.query = Event.query
            activity_id = form.activity.data
            event_id = form.event.data
            new_customer = Customer(first_name=first_name, last_name=last_name, email=email, telephone_number=telephone_number)
            print(new_customer)
            classbooking = Booking(activity_id=activity_id, event_id=event_id, dog_name=dog_name, customer=new_customer)
            print(classbooking)
            dogbooked = Dog(customer=new_customer, dog_name=classbooking.dog_name)
            print(dogbooked)
            # service.add_new_customer(customer)
            service.add_new_booking(new_customer, classbooking, dogbooked)
            if form.validate_on_submit():
                return "Thanks! You're signed up!"
    return render_template('classes', form=form)

@app.route("/recommendations", methods=['GET', 'POST'])
def user_info():
    form = recommendation_form()
    if request.method == 'GET':
        form = recommendation_form()
        dog_name = form.dog_name.data
        breed = form.breed.data
        age = form.age.data
        size = form.size.data
        temperament = form.temperament.data
        return render_template('recommendations.html', form=form, dog_name=dog_name, breed=breed, age=age, size=size, temperament=temperament)
    if request.method == 'POST':
        dog_name = form.dog_name.data
        breed = form.breed.data
        age = form.age.data
        size = form.size.data
        temperament = form.temperament.data
        return render_template('recommendations.html', form=form, dog_name=dog_name, breed=breed, age=age, size=size, temperament=temperament)







#@app.route('/testing', methods=['GET', 'POST'])
#def test():
    #select = request.args.get('Select2')
    #print(str(select))
    #return str(select)


