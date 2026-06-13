import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)

    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    from . import blog
    app.register_blueprint(blog.bp)


    @app.route("/init-db/")
    def init_db():
        from . import db
        db.init_db()
        return "Base de datos inicializada"
    
    @app.route("/")
    def index():
        return render_template("home/index.html")

    return app