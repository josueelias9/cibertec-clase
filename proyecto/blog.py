

from flask import Blueprint, render_template


bp = Blueprint("blog", __name__, url_prefix="/cibertec")

@bp.route("/mostrar-blog")
def mostrar_blog():
    return render_template("blog/blog.html")


@bp.route("/eliminar-blog")
def eliminar_blog():
    pass

@bp.route("/update-blog")
def update_blog():
    pass