import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)

    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    @app.route("/")
    def index():
        # Cargar contador
        f = open("count.txt", "r")
        count = int(f.read())
        f.close()
        # Incrementar el contador
        count += 1
        # Actualizar
        f = open("count.txt", "w")
        f.write(str(count))
        f.close()
        # Pasar la variable actualizada a index.html
        return render_template("index.html", count=count)

    @app.route("/ejemplo-json")
    def ejemplo_json():
        return {"mensaje": "Hola, este es un ejemplo de respuesta JSON"}



    @app.route("/mostrar-blog")
    def mostrar_blog():
        return render_template("blog/blog.html")


    @app.route("/init-db/")
    def init_db():
        from . import db
        db.init_db()
        return "Base de datos inicializada"

    return app