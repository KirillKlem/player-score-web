from flask import Flask
from main.extensions import db, migrate


def create_app(config_object="main.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)


    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None
