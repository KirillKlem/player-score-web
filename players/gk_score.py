from .count_score import get_names, get_all_stats, get_type_of_stats, \
    count_score_of_types, add_to_all_score, add_to_final_score, count_total_score, \
    create_weighted_average
from . import constants

from pprint import pprint

def count_gk_score():
    gk_names = get_names('GK')
    goalkeeper_stats = get_all_stats(gk_names)
    all_gk_score = {player: [] for player in gk_names}
    final_gk_score = {player: {} for player in gk_names}



    def count_group_stats(main_constant):
        weighted_average = {}
        for constant in getattr(constants, main_constant):
            weighted_average[constant.lower()] = create_weighted_average(gk_names, goalkeeper_stats, getattr(constants, constant))

        result_stats_gk = count_score_of_types(gk_names, weighted_average, getattr(constants, main_constant))
        pprint(result_stats_gk)
        #     add_to_all_score(result_stats_gk, all_gk_score)

        # add_to_final_score(main_constant.lower(), final_gk_score, all_gk_score)
            

    count_group_stats('TEAM_INFLUENCE_GK')
    # count_total_score(gk_names, final_gk_score, all_gk_score)
    # pprint(all_gk_score)
    # pprint(final_gk_score)



        
