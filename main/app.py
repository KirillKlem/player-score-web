from flask import Flask, request, jsonify
from main.extensions import db, migrate


def create_app(config_object="main.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)

    @app.route('/api/player', methods=['POST'])
    def save_player():
        print(request.json)
        return jsonify({'status': 'created'}), 201
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None
