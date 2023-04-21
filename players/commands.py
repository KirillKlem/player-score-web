from main.extensions import db
from .models import Player

import click

@click.command()
def print_gk():
    player_names = []

    players = db.session.execute(db.select(Player).filter_by(pos='GK')).scalars()
    for player in players:
        player_names.append(player)

    print(player_names)
    