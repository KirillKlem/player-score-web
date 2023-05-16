from flask import Flask
from flask_admin.contrib.sqla import ModelView

import players
from main.extensions import admin, db, ma, migrate
from players.models import Attacking, Defender, Goalkeeper, Midfielder


def create_app(config_object="main.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_admin()

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    admin.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(players.views.blueprint)
    return None


def register_commands(app):
    app.cli.add_command(players.commands.count_score)


def register_admin():
    admin.add_view(ModelView(Goalkeeper, db.session))
    admin.add_view(ModelView(Defender, db.session))
    admin.add_view(ModelView(Midfielder, db.session))
    admin.add_view(ModelView(Attacking, db.session))
