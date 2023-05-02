from .count_score import get_names, get_all_stats, get_type_of_stats, \
    count_score_of_types, add_in_all_score, count_score
from . import constants

from pprint import pprint

def count_gk_score():
    gk_names = get_names('GK')
    goalkeeper_stats = get_all_stats(gk_names)
    all_gk_score = {player: [] for player in gk_names}


    def count_group_stats(need_constant):
        for stats in getattr(constants, need_constant):
            stats_gk = get_type_of_stats(goalkeeper_stats, getattr(constants, stats))
            result_stats_gk = count_score_of_types(gk_names, stats_gk)

            add_in_all_score(result_stats_gk, all_gk_score)


    count_group_stats('TEAM_INFLUENCE_GK')
    final_gk_score = count_score(gk_names, all_gk_score)
    pprint(final_gk_score)


        
