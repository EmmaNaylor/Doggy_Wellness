import json
from flask import render_template, request, jsonify, escape
from application import service
from application import app
from application.forms.signUp import SignUpForm
from application.models.customer import Customer
from application.models.dog import Dog

@app.route('/', methods=['GET'])
def hello():
    return render_template("home.html", title="Home")


@app.route('/activity', methods=['GET'])
def show_activities():
    error = ""
    details = service.activities()
    if len(details) == 0:
        error = "There are no books to display"
    return render_template('test.html', activities=details, message=error)


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


@app.route("/recommend/<size>")
def give_recommendation(size):
    if size == "small":
        amount = "once a week"
        return str(amount)
    elif size == "medium":
        amount = "twice a week"
        return str(amount)
    elif size == "large":
        amount = "three times a week"
        return str(amount)


@app.route('/signup', methods=['GET', 'POST'])
def book_a_class():
    error = ""
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.form)
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        telephone_number = form.telephone_number.data
        dog_name = form.dog_name.data

        if len(dog_name) == 0 or len(first_name) == 0:
            error = "Please supply both your name and your dog's name"
        else:
            customer = Customer(first_name=first_name, last_name=last_name, email=email, telephone_number=telephone_number, dog_name=dog_name)
            service.add_new_customer(customer)
    return render_template('new_customer_form.html', form=form, message=error)
