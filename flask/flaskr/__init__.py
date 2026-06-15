import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )


    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)


    from .db import db_session, init_db

    @app.route("/init-db/")
    def init_my_db():
        init_db()
        return "Base de datos inicializada"
    
    @app.route("/")
    def index():
        return render_template("home/index.html")


    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    from . import blog
    from . import auth
    
    app.register_blueprint(blog.bp)
    app.register_blueprint(auth.bp)


    return app