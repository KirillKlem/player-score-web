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

TEAM_INFLUENCE_GK = {
    'DIRECT_TEAM_INFLUENCE_GK': 45, 
    'DEFENSIVE_TEAM_INFLUENCE_GK': 65,
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

PASSING_GK = {
    'PASSING_OVERALL_GK': 33,
    'PASSING_SHORT_GK': 50,
    'PASSING_MEDIUM_GK': 40,
    'PASSING_LONG_GK': 28,
    'PASSING_ATACKING_GK': 17,
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

GOALKEEPING_GK = {
    'ALLOWED_GOALKEEPING_GK': 40,
    'SAVES_GOALKEEPING_GK': 95,
    'PENALTY_SAVES_GOALKEEPING_GK': 10,
}

TOTAL_SCORE_GK = {
    'TEAM_INFLUENCE_GK': 10,
    'PASSING_GK': 40,
    'GOALKEEPING_GK': 95,
}

NEGATIVE_PLAYER_STATS = ['performance_ga', 'performance_ga90', 'penalty_kicks_pka']