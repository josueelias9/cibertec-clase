

from flask import Blueprint, render_template, request
from .db import get_db

bp = Blueprint("blog", __name__, url_prefix="/cibertec")

@bp.route("/mostrar-blog", methods=["GET"])
def mostrar_blog():
    return render_template("blog/blog.html")



@bp.route("/index")
def index():
    db = get_db()
    posts = db.execute(
        "SELECT * FROM post"
    ).fetchall()
    return render_template("blog/index.html", posts=posts)


@bp.route("/create", methods=["GET", "POST"])
def create_blog():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        author_id = 1
        db = get_db()
        db.execute(
            "INSERT INTO post (title, body, author_id) VALUES (?, ?,?)",
            (title, body, author_id)
        )
        # Aquí se procesaría el formulario para crear una nueva entrada de blog
        return {"info":"Nueva entrada de blog creada"}
    return render_template("blog/create.html")

@bp.route("/eliminar-blog")
def eliminar_blog():
    pass

@bp.route("/update-blog")
def update_blog():
    pass