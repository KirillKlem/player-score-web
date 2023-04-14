from flask import Blueprint, request, jsonify, render_template
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
        db.session.add(player)
        db.session.commit()
        return jsonify({'status': 'created'}), 201
    return jsonify({'error': f'Position {position} does not exists'}), 400


@blueprint.route('/')
def get_players_list():
    players = db.session.execute(db.select(Player)).scalars()
    title = 'Список игроков'
    return render_template('index.html', players=players, title=title)


@blueprint.route('/<int:id_>')
def get_player_details(id_):
    player = db.get_or_404(Player, id_)
    title = player.name
    fields = attribute_names(player.__class__)
    return render_template('detail.html', player=player, title=title, fields=fields, getattr=getattr)