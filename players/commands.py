from main.extensions import db
from .models import Player
from .gk_score import count_gk_score
from .def_score import count_def_score

import click

@click.command()
def count_score():
    count_gk_score()
    count_def_score()