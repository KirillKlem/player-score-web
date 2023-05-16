from .count_score import create_models, get_names, get_all_stats, count_main_weighted_average, \
    add_to_all_score, add_to_final_score, count_total_score, create_weighted_average, update_db
from . import constants

from pprint import pprint

def count_def_score():
    df_names = get_names(position='DF', condition=200)
    df_models = create_models(df_names)
    df_stats = get_all_stats(df_names)
    all_df_score = {df: {} for df in df_names}
    final_df_score = {df: {} for df in df_names}

    # Note:
    # Основная часть не работает пока не добавлены константы!!!

    # def count_group_stats(main_constant):
    #     weighted_average = {}
    #     for constant in getattr(constants, main_constant):
    #         weighted_average[constant.lower()] = create_weighted_average(df_names, df_stats, getattr(constants, constant))
    #         add_to_all_score(weighted_average, all_df_score)

    #     result_stats_gk = count_main_weighted_average(df_names, weighted_average, getattr(constants, main_constant))
    #     add_to_final_score(main_constant.lower(), result_stats_gk, final_df_score)
            
    # for const in constants.TOTAL_SCORE_DF:
    #     count_group_stats(const)

    # count_total_score(final_df_score, getattr(constants, 'TOTAL_SCORE_GK'))
    # update_db(player_models=df_models, player_score=final_df_score)
