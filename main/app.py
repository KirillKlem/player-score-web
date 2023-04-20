from flask import Flask
from main.extensions import db, migrate, ma
import players




def create_app(config_object="main.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    return None

def register_blueprints(app):
    app.register_blueprint(players.views.blueprint)
    return None

def register_commands(app):
    app.cli.add_command(players.commands.print_gk)
