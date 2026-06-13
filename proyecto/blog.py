

from flask import Blueprint, render_template, request
from .db import get_db

bp = Blueprint("blog", __name__, url_prefix="/cibertec")



@bp.route("/index")
def index():
    db = get_db()
    posts = db.execute(
        "SELECT * FROM post"
    ).fetchall()
    return render_template("blog/index.html", posts=posts)


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        author_id = 1
        db = get_db()
        db.execute(
            "INSERT INTO post (title, body, author_id) VALUES (?, ?,?)",
            (title, body, author_id)
        )
        db.commit()
        # Aquí se procesaría el formulario para crear una nueva entrada de blog
        return {"info":"Nueva entrada de blog creada"}
    return render_template("blog/create.html")

@bp.route("/<int:id>/delete", methods=("POST",))
def delete(id):
    post = get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    return {"info":"Entrada de blog eliminada"}

@bp.route("/<int:id>/update", methods=("GET", "POST"))
def update(id):
    post = get_post(id)
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]

        db = get_db()
        db.execute(
            "UPDATE post SET title = ?, body = ? WHERE id = ?",
            (title, body, id)
        )
        db.commit()
        return {"info":"Entrada de blog actualizada"}
    return render_template("blog/update.html", post=post)


def get_post(id):
    db = get_db()
    post = db.execute(
        "SELECT * FROM post WHERE id = ?", (id,)
    ).fetchone()

    return post




# http:127.0.0.1:5000/cibertec/2/delete
# http:127.0.0.1:5000/cibertec/1/delete
# http:127.0.0.1:5000/cibertec/10/delete