import json
import mysql.connector
import pymysql
from flask_wtf import FlaskForm
from flask import render_template, request, jsonify, escape, url_for, redirect, flash
from application import service
from application import app
from application.forms.signUp import SignUpForm
from application.forms.booking import BookingForm
from application.models.activity import Activity
from application.models.customer import Customer
from application.models.dog import Dog
from application.models.member import Member
from application.models.booking import Booking
from application.models.event_info import Event
from application.forms.login import LoginForm
from application.forms.recommendation_form import Recommendation_Form
from application.forms.register import RegisterForm
from flask_bootstrap import Bootstrap
from wtforms_sqlalchemy.fields import QuerySelectField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from email_validator import validate_email, EmailNotValidError


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = SignUpForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            flash("Thanks! You're signed up!")
            redirect(url_for("home"))
        form = SignUpForm(request.form)
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        telephone_number = form.telephone_number.data
        recaptcha = form.recaptcha
        customer = Customer(first_name=first_name, last_name=last_name, email=email, telephone_number=telephone_number)
        service.add_new_customer(customer)
    return render_template('index', form=form, title="Home")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.form)
        email = form.email.data
        user_password = form.password.data
        if form.validate_on_submit():
            member = Member.query.filter_by(email=form.email.data).first()
            if check_password_hash(member.user_password, form.password.data):
                login_user(member)
                if member.email == "theadministator@gmail.com":
                    return redirect(url_for('display_all_bookings'))
                else:
                    return redirect(url_for('display_customer_bookings'))
            flash("Invalid username or password")
            return redirect(url_for('login'))
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
            customer_check = Customer.query.filter_by(email=form.email.data).first()
            if member_check:
                flash("Email is already in use")
                return redirect(url_for('signup'))
            if customer_check:
                new_member = Member(email=email, user_password=hashed_password)
            service.add_new_member(new_member)
            return redirect(url_for('login'))
    return render_template('signup', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = Recommendation_Form()
    if request.method == 'POST' and form.validate():
        form = Recommendation_Form()
        dog_name = form.dog_name.data
        breed = form.breed.data
        age = form.age.data
        size = form.size.data
        temperament = form.temperament.data
        amount = service.size_check(size)
        recommendation = service.fav_class(temperament)
        return render_template('recommendations', form=form, dog_name=dog_name, breed=breed, age=age, size=size, temperament=temperament, amount=amount, recommendation=recommendation)
    return render_template('recommendations', form=form)


@app.route('/classes', methods=['GET', 'POST'])
def booking():
    form = BookingForm()
    if request.method == 'POST':
            form = BookingForm()
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
            classbooking = Booking(activity_id=activity_id, event_id=event_id, dog_name=dog_name, customer=new_customer)
            print(classbooking)
            dogbooked = Dog(customer=new_customer, dog_name=classbooking.dog_name)
            service.add_new_booking(new_customer, classbooking, dogbooked)
            if form.validate_on_submit():
                flash("Thanks! You're signed up!")
                return redirect(url_for('booking'))
    return render_template('classes', form=form, Title="Classes")


@app.route('/admin-dashboard', methods=['GET'])
@login_required
def display_all_bookings():
    all_bookings = service.display_all_bookings()
    return render_template('admindashboard.html', all_bookings=all_bookings)


@app.route('/customer-dashboard', methods=['GET'])
@login_required
def display_customer_bookings():
    user = current_user.linked_customer
    print(user)
    customer_name = service.name(user)
    print("name", customer_name)
    customer_bookings = service.display_customer_bookings(user)
    return render_template('customerdashboard.html', customer_bookings=customer_bookings, name=customer_name)


@app.route('/layout')
def layout():
    return render_template('layout.html')


# @app.route('/activity', methods=['GET'])
# def show_activities():
#     error = ""
#     details = service.activities()
#     if len(details) == 0:
#         error = "There are no activities to display"
#     return render_template('test.html', activities=details)
#
#
# @app.route("/recommend")
# def recommend():
#     size = (request.args.get("size", ""))
#     if size:
#         answer = give_recommendation(size)
#     else:
#         answer = ""
#     return (
#             """<form action="" method="get">
#               <input type="text" name="size" />
#               <input type="submit" value="Give me a recommendation">
#               </form>"""
#             + "You should exercise your dog: "
#             + answer
#     )


# @app.route("/recommendation", methods=['GET', 'POST'])
# def give_recommendation():
#     conn = pymysql.connect(host='localhost', user='root', passwd='password', db='dog_wellness_service')
#     cursor = conn.cursor()
#     cursor.execute('SELECT size FROM dog_category')
#     sizelist = cursor.fetchall()
#     return render_template('testing2.html', sizelist=sizelist)