from flask import Flask, render_template
from main.extensions import db, migrate


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        title = 'Рейтинги футбольных игроков:'
        return render_template('index.html', title=title)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None
