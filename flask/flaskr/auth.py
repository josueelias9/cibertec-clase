
from datetime import datetime
from flask import Blueprint, request, jsonify
from .db import db_session

bp = Blueprint("auth", __name__, url_prefix="/auth")


from .models import User

@bp.route("/")
def index():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@bp.route("/create", methods=("POST",))
def create():
    try:
        username = request.form["username"]
        password = request.form["password"]
        user = User(username=username, password=password)
        db_session.add(user)
        db_session.commit()
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:id>/update", methods=("POST",))
def update(id):
    try:
        user = User.query.filter_by(id=id).first()
        username = request.form["username"]
        password = request.form["password"]
        user.username = username
        user.password = password
        db_session.commit()
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:id>/delete", methods=("POST",))
def delete(id):
    try:
        user = User.query.filter_by(id=id).first()
        db_session.delete(user)
        db_session.commit()
        return jsonify({"message": "User deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400