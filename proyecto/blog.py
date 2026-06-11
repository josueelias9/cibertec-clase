

from flask import Blueprint, render_template, request
from .db import get_db

bp = Blueprint("blog", __name__, url_prefix="/cibertec")

@bp.route("/mostrar-blog")
def mostrar_blog():
    return render_template("blog/blog.html")


@bp.route("/create", methods=["GET", "POST"])
def create_blog():
    if request.method == "POST":
        titulo = request.form["titulo"]
        contenido = request.form["content"]
        author_id = 1
        db = get_db()
        db.execute(
            "INSERT INTO post (title, body, author_id) VALUES (?, ?,?)",
            (titulo, contenido,author_id)
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