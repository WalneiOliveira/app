from app import app

from flask import render_template
from flask import request

@app.route("/")
def index():
    return render_template("/public/index.html")


@app.route("/about")
def about():
    return render_template("/public/templates/about.html")


@app.route("/subscribe")
def subscribe():
    title = "Subscribe To My Email Newsletter"
    return render_template("/public/templates/subscribe.html", title=title)


@app.route("/form", methods = ["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email= request.form.get("email")
    title = "Thank You"
    return render_template("/public/templates/form.html", title=title, form=form, first_name=first_name, last_name=last_name, email=email)

    