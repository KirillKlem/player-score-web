from flask import Blueprint, request, jsonify
from .models import Player

blueprint = Blueprint('players', __name__)

@blueprint.route('/api/player', methods=['POST'])
def save_player():
    print(request.json)
    return jsonify({'status': 'created'}), 201
