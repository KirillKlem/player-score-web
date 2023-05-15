from .count_score import get_names, get_all_stats, count_main_weighted_average, \
    add_to_all_score, add_to_final_score, count_total_score, create_weighted_average
from . import constants

from pprint import pprint

def count_gk_score():
    '''
    "all_gk_score" contains all the calculated values
    "final_gk_score" contains the main calculated values (including 'total')

    ...
    '''

    gk_names = get_names('GK')
    goalkeeper_stats = get_all_stats(gk_names)
    all_gk_score = {player: {} for player in gk_names}
    final_gk_score = {player: {} for player in gk_names}

    def count_group_stats(main_constant):
        weighted_average = {}
        for constant in getattr(constants, main_constant):
            weighted_average[constant.lower()] = create_weighted_average(gk_names, goalkeeper_stats, getattr(constants, constant))
            add_to_all_score(weighted_average, all_gk_score)

        result_stats_gk = count_main_weighted_average(gk_names, weighted_average, getattr(constants, main_constant))
        add_to_final_score(main_constant.lower(), result_stats_gk, final_gk_score)
            
    for const in constants.TOTAL_SCORE_GK:
        count_group_stats(const)

    count_total_score(final_gk_score, getattr(constants, 'TOTAL_SCORE_GK'))
