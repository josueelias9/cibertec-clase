


from flask import Blueprint, render_template, request, redirect, flash
from .db import db_session
from .models import User
bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif User.query.filter_by(username=username).first() is not None:
            error = f"User {username} is already registered."

        if error is None:
            user = User(username=username, password=password)
            db_session.add(user)
            db_session.commit()
            return redirect("/")

        flash(error)
    return render_template("auth/register.html")

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = "Incorrect username."
        elif user.password != password:
            error = "Incorrect password."

        if error is None:
            return redirect("/")

        flash(error)
    return render_template("auth/login.html")