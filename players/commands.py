from main.extensions import db
from .models import Player
from .gk_score import count_gk_score

import click

@click.command()
def print_gk():
    count_gk_score()
    