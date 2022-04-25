import json
import mysql.connector
import pymysql
from flask import render_template, request, jsonify, escape
from application import service
from application import app
from application.forms.signUp import SignUpForm
from application.forms.booking import bookingForm
from application.models.activity import Activity
from application.models.customer import Customer
from application.models.dog import Dog
from application.models.booking import Booking
from application.models.event_info import Event


# @app.route('/', methods=['GET'])
# def index():
#     return render_template("index.html", title="Home")


@app.route('/classes', methods=['GET'])
def classes():
    return render_template("classes.html", title="Classes")


@app.route('/recommendations', methods=['GET'])
def recommendations():
    return render_template("recommendations.html", title="Recommendations")


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
def sign_up():
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
    return render_template("index.html", form=form, title="Home")


@app.route('/bookaclass', methods=['GET', 'POST'])
def booking():
    form = bookingForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            return "Thanks! You're signed up!"
        form = bookingForm(request.form)
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        telephone_number = form.telephone_number.data
        recaptcha = form.recaptcha
        # dog_name = form.dog_name.data
        # form.activity.query = Activity.query.all
        # form.event.query = Event.query.all
        # activity_id = form.activity.query
        # event_id = form.event.query
        customer = Customer(first_name=first_name, last_name=last_name, email=email, telephone_number=telephone_number)
        # classbooking = Booking(activity_id=activity_id, event_id=event_id, dog_name=dog_name)
        service.add_new_customer(customer)
        # service.add_new_booking(classbooking)
    return render_template('bookingformtest.html', form=form)
