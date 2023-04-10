from flask import Blueprint, request, jsonify
from .models import Player
from main.extensions import db

blueprint = Blueprint('players', __name__)

@blueprint.route('/api/player', methods=['POST'])
def save_player():
    print(request.json)
    return jsonify({'status': 'created'}), 201


@blueprint.route('/api/player/<position>', methods=['POST'])
def test_player(position):
    models = {
        mapper.class_.__mapper_args__["polymorphic_identity"]:mapper.class_
        for mapper in db.Model.registry.mappers
    }
    position = position.upper()
    if position in models:
        player = models[position](**request.json)
    db.session.add(player)
    db.session.commit()
    return 'Ok!'