from .count_score import count_stat, get_name_players
from main.extensions import db
from .models import Player, Goalkeeper


goalkeeper_names = get_name_players('GK')
def count_score():
    print(goalkeeper_names)
