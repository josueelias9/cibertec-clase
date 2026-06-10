from flask import Blueprint, render_template, request, redirect, url_for
from .db import get_db

bp = Blueprint("blog", __name__, url_prefix="/blog")



@bp.route("/index")
def ver_blog():
    db = get_db()  # Obtener la conexión a la base de datos
    posts = db.execute("SELECT * FROM post").fetchall()
    return render_template("blog/index.html", posts=posts)


@bp.route("/create", methods=["GET", "POST"])
def crear_blog():
    if request.method == "POST":
        # Aquí puedes manejar la lógica para guardar el blog en la base de datos
        titulo = request.form["title"]
        contenido = request.form["content"]
        author_id = 1  # Suponiendo que el autor es el usuario con ID 1 (puedes cambiar esto según tu lógica de autenticación)
        db = get_db()  # Obtener la conexión a la base de datos
        db.execute(
            "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)", (titulo, contenido, author_id)
        )
        db.commit()  # Guardar los cambios en la base de datos
        # Guardar el blog en la base de datos (lógica no implementada)
        return redirect("index")  # Redirigir a la página de ver blogs después de crear uno nuevo
    return render_template("blog/create.html")



@bp.route("/<int:id>/update", methods=["GET", "POST"])
def update_blog(id):
    db = get_db()
    post = db.execute("SELECT * FROM post WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        titulo = request.form["title"]
        contenido = request.form["body"]
        db.execute(
            "UPDATE post SET title = ?, body = ? WHERE id = ?", (titulo, contenido, id)
        )
        db.commit()
        return redirect(url_for("blog.ver_blog"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=["POST"])
def delete_blog(id):
    id = request.form["id"]
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect("index")