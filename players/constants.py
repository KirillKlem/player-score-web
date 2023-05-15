DIRECT_TEAM_INFLUENCE_GK = {
    'team_success_on_minus_off': 10,
    'team_success_ong': 10,
    'team_success_onga': 10,
    'team_success_plus_in_minus': 0,
    'team_success_plus_in_minus_90': 50,
    'team_success_ppm': 30,
    'team_success_xg_on_minus_off': 0,
    'team_success_xg_onxg': 20,
    'team_success_xg_onxga': 20,
    'team_success_xg_xg_plus_in_minus': 0,
    'team_success_xg_xg_plus_in_minus_90': 50,
}

DEFENSIVE_TEAM_INFLUENCE_GK = {
    'touches_def_3rd': 30, 
    'touches_def_pen': 30,
    'total_att': 60, 
}

PASSING_OVERALL_GK = {
    'total_cmp': 20,
    'total_cmp_percent': 80,
    'total_prgdist': 65,
    'total_totdist': 55,
}

PASSING_SHORT_GK = {
    'short_att': 35,
    'short_cmp': 45,
    'short_cmp_percent': 70,
}

PASSING_MEDIUM_GK = {
    'medium_att': 40,
    'medium_cmp': 50,
    'medium_cmp_percent': 70,
}

PASSING_LONG_GK = {
    'long_att': 20,
    'long_cmp': 40,
    'long_cmp_percent': 90,
}

PASSING_ATACKING_GK = {
    'ast': 5,
    'xa': 5,
    'xag': 5,
    'kp': 30,
    'on1_in_3': 40,
    'ppa': 20,
    'prgp': 50,
}

ALLOWED_GOALKEEPING_GK = {
    'performance_ga': 50,
    'performance_ga90': 50,
}

SAVES_GOALKEEPING_GK = {
    'performance_save_percent': 95,
    'performance_saves': 90,
    'performance_cs': 30,
    'performance_cs_percent': 35,
}

PENALTY_SAVES_GOALKEEPING_GK = {
    'penalty_kicks_pksv': 50,
    'penalty_kicks_save_percent': 75,
    'penalty_kicks_pka': 10,
}

SPECIAL_GOALS_GK = {
    'goals_ck': 10,
    'goals_fk': 10,
    'goals_og': 10,
}

PSXG_GK = {
    'expected_psxg_plus_in_minus': 95,
    'expected_psxg_in_sot': 10,
}

DEFENSIVE_ACTIONS_GK = {
    'sweeper_avgdist': 35,
    'sweeper_opa': 90,
}

LAUNCHED_GK = {
    'launched_att': 40,
    'launched_cmp': 35,
    'launched_cmp_percent': 80,
}

THROWS_GK = {
    'passes_att': 50,
    'passes_avglen': 65,
    'passes_launch_percent': 30,
    'passes_thr': 30,
}

GOAL_KICKS_GK = {
    'goal_kicks_att': 10,
    'goal_kicks_avglen': 20,
    'goal_kicks_launch_percent': 20,
}

CROSSES_GK = {
    'crosses_opp': 10,
    'crosses_stp': 50,
    'crosses_stp_percent': 90,
}

TEAM_INFLUENCE_GK = {
    'DIRECT_TEAM_INFLUENCE_GK': 45, 
    'DEFENSIVE_TEAM_INFLUENCE_GK': 65,
}

GENERAL_PASSING_GK = {
    'PASSING_OVERALL_GK': 33,
    'PASSING_SHORT_GK': 50,
    'PASSING_MEDIUM_GK': 40,
    'PASSING_LONG_GK': 28,
    'PASSING_ATACKING_GK': 17,
}

GOALKEEPING_GK = {
    'ALLOWED_GOALKEEPING_GK': 40,
    'SAVES_GOALKEEPING_GK': 95,
    'PENALTY_SAVES_GOALKEEPING_GK': 10,
}

ADVANCED_GOALKEEPING_GK = {
    'SPECIAL_GOALS_GK': 20,
    'PSXG_GK': 80,
    'DEFENSIVE_ACTIONS_GK': 40,
}

ADVANCED_PASSING_GK = {
    'LAUNCHED_GK': 45,
    'THROWS_GK': 25,
    'GOAL_KICKS_GK': 10,
    'CROSSES_GK': 40,
}

TOTAL_SCORE_GK = {
    'TEAM_INFLUENCE_GK': 10,
    'GENERAL_PASSING_GK': 50,
    'GOALKEEPING_GK': 95,
    'ADVANCED_GOALKEEPING_GK': 40,
    'ADVANCED_PASSING_GK': 40,
}

NEGATIVE_PLAYER_STATS = ['performance_ga', 'performance_ga90', 'penalty_kicks_pka', 'goals_ck',
                         'goals_fk', 'goals_og', 'expected_psxg_in_sot']