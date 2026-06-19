
from datetime import datetime
from flask import Blueprint, render_template, request, redirect,jsonify
from .db import db_session

bp = Blueprint("blog_json", __name__, url_prefix="/blog_json")


from .models import Post

@bp.route("/")
def index():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])



@bp.route("/create", methods=("POST",))
def create():
    try:
        title = request.form["title"]
        body = request.form["body"]
        post = Post(title=title, body=body, author_id=1, created=datetime.now())
        db_session.add(post)
        db_session.commit()
        return jsonify(post.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:id>/update", methods=("POST",))
def update(id):
    try:
        post = Post.query.filter_by(id=id).first()
        post.title = request.form["title"]
        post.body = request.form["body"]
        db_session.commit()
        return jsonify(post.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@bp.route("/<int:id>/delete", methods=("POST",))
def delete(id):
    try:
        post = Post.query.filter_by(id=id).first()
        db_session.delete(post)
        db_session.commit()
        return jsonify(post.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 400



