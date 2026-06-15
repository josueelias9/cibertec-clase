
from datetime import datetime
from flask import Blueprint, render_template, request, redirect
from .db import db_session

bp = Blueprint("blog", __name__, url_prefix="/blog")


from .models import Post

@bp.route("/index")
def index():
    posts = Post.query.all()
    return render_template("blog/index.html", posts=posts)



@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        post = Post(title=title, body=body, author_id=1, created=datetime.now())
        db_session.add(post)
        db_session.commit()
        # Aquí se procesaría el formulario para crear una nueva entrada de blog
        return redirect("/blog/index")
    return render_template("blog/create.html")


@bp.route("/<int:id>/delete", methods=("POST",))
def delete(id):
    post = get_post(id)
    db_session.delete(post)
    db_session.commit()
    return redirect("/blog/index")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
def update(id):
    post = get_post(id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.body = request.form["body"]

        db_session.commit()

        return redirect("/blog/index")
    return render_template("blog/update.html", post=post)


def get_post(id):
    post = Post.query.filter_by(id=id).first()
    return post


