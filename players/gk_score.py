from main.extensions import db
from .models import Player
from .count_score import get_names, create_players, get_all_stats

from pprint import pprint

def count_gk_score():
    gk_names = get_names('GK')
    goalkeepers = create_players(gk_names)
    goalkeeper_stats = get_all_stats(goalkeepers)
    
    pprint(goalkeeper_stats)

