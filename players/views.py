from flask import Blueprint, request, jsonify
from .models import Player
from main.extensions import db
from .utils import attribute_names

blueprint = Blueprint('players', __name__)

@blueprint.route('/api/player/<position>', methods=['POST'])
def save_player(position):
    models = {
        mapper.class_.__mapper_args__["polymorphic_identity"]: mapper.class_
        for mapper in db.Model.registry.mappers
    }
    position = position.upper()
    if position in models:
        model = models[position]
        fields = attribute_names(model)
        json_data = request.json.items()

        player = model(**{k: v for k, v in json_data if k in fields})
        exists = db.session.query(Player.name).filter_by(name=player.name).first() is not None

        if exists:
            print('exists')
            Player.query.filter_by(name=player.name).first().update(player)
        else:
            print('not exists')
            db.session.add(player)

        db.session.commit()

        return jsonify({'status': 'created'}), 201
    return jsonify({'error': f'Position {position} does not exists'}), 400