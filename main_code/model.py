from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class Player(db.Model):
    __tablename__ = 'player'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column()
    age: Mapped[int]
    position: Mapped[str] = mapped_column()
    matches: Mapped[int]
    minutes: Mapped[int]
    goals: Mapped[int]
    assists: Mapped[int]
    y_cards: Mapped[int]
    r_cards: Mapped[int]
    touches: Mapped[int]
    touches_def_pen: Mapped[int]
    touches_def_3rd: Mapped[int]
    touches_mid_3rd: Mapped[int]
    touches_att_3rd: Mapped[int]
    touches_att_pen: Mapped[int]
    carries: Mapped[int]
    total_carrying_dist: Mapped[int]
    progressive_carrying_dist: Mapped[int]
    progressive_carries: Mapped[int]
    carries_att_3rd: Mapped[int]
    miscontrols: Mapped[int]
    dispossessed: Mapped[int]
    progressive_passes_rec: Mapped[int]
    percentage_minutes: Mapped[float]
    games_start: Mapped[int]
    points_per_match: Mapped[float]
    goals_plus_minus_net: Mapped[float]
    xG_plus_minus_net: Mapped[float]

    __mapper_args__ = {
        "polymorphic_identity": "player",
        "polymorphic_on": position
    }

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


class Goalkeeper(Player):
    __tablename__ = 'goalkeepers'

    id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
    goalkeeper_name: Mapped[str] = mapped_column(key='player.name')
    goals_against: Mapped[int]
    shots_against: Mapped[int]
    saves: Mapped[int]
    saves_percentage: Mapped[float]
    clean_sheets: Mapped[int]
    clean_sheets_percentage: Mapped[float]
    saves_penalty_kicks: Mapped[int]
    saves_penalty_kicks_percentage: Mapped[float]
    goals_free_kick_against: Mapped[int]
    goals_corner_kick_against: Mapped[int]
    PSxG: Mapped[float]
    PSxg_per_SoT: Mapped[float]
    PSxG_plus_minus: Mapped[float]
    passes_launched: Mapped[int]
    passes_launched_completion_percentage: Mapped[float]
    passes_launched_percentage_notGoalKick: Mapped[float]
    average_pass_length: Mapped[float]
    average_pass_length_GoalKick: Mapped[float]
    crosses_stopped: Mapped[int]
    def_actions_OutOfPenArea: Mapped[int]
    average_dist_def_actions: Mapped[float]

    __mapper_args__ = {
        "polymorphic_identity": "GK"
    }


class Center_Back(Player):
    __tablename__ = 'center_backs'

    id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
    center_defender_name: Mapped[str] = mapped_column(key='player.name')
    passes: Mapped[int]
    passes_completion: Mapped[float]
    total_passing_dist: Mapped[int]
    progressive_passing_disc: Mapped[int]
    short_passes: Mapped[int]
    short_passes_completion: Mapped[float]
    medium_passes: Mapped[int]
    medium_passes_completion: Mapped[float]
    long_passes: Mapped[int]
    long_passes_completion: Mapped[float]
    progressive_passes: Mapped[int]
    tackles: Mapped[int]
    tackles_won: Mapped[int]
    tackles_def_3rd: Mapped[int]
    tackles_mid_3rd: Mapped[int]
    dribblers_tackles_won: Mapped[int]
    dribblers_tackles_attemped: Mapped[int]
    dribblers_tackles_won_percentage: Mapped[float]
    blocks: Mapped[int]
    shots_blocks: Mapped[int]
    passes_blocks: Mapped[int]
    interceptions: Mapped[int]
    errors: Mapped[int]
    clearances: Mapped[int]
    fouls: Mapped[int]
    recoveries: Mapped[int]
    air_duels_won: Mapped[int]
    air_duels_won_percentage: Mapped[float]

    __mapper_args__ = {
        "polymorphic_identity": "CB"
    }


class Moderately_Attacking(Player):
    __tablename__ = 'moderately_attacking_defenders'

    id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
    attacking_defender_name: Mapped[str] = mapped_column(key='player.name')
    passes: Mapped[int]
    passes_completion: Mapped[float]
    total_passing_dist: Mapped[int]
    progressive_passing_disc: Mapped[int]
    short_passes: Mapped[int]
    short_passes_completion: Mapped[float]
    medium_passes: Mapped[int]
    medium_passes_completion: Mapped[float]
    long_passes: Mapped[int]
    long_passes_completion: Mapped[float]
    progressive_passes: Mapped[int]
    passes_att_3rd: Mapped[int]
    carries_into_penalty_area: Mapped[int]
    key_passes: Mapped[int]
    crosses_penalty_area: Mapped[int]
    through_passees: Mapped[int]
    switches: Mapped[int]
    crosses: Mapped[int]
    tackles: Mapped[int]
    tackles_won: Mapped[int]
    tackles_def_3rd: Mapped[int]
    tackles_mid_3rd: Mapped[int]
    tackles_att_3rd: Mapped[int]
    dribblers_tackles_won: Mapped[int]
    dribblers_tackles_attemped: Mapped[int]
    dribblers_tackles_won_percentage: Mapped[float]
    blocks: Mapped[int]
    shots_blocks: Mapped[int]
    passes_blocks: Mapped[int]
    interceptions: Mapped[int]
    errors: Mapped[int]
    clearances: Mapped[int]
    fouls: Mapped[int]
    recoveries: Mapped[int]
    air_duels_won: Mapped[int]
    air_duels_won_percentage: Mapped[float]
    shot_creating_actions: Mapped[int]
    goal_creating_actions: Mapped[int]

    __mapper_args__ = {"polymorphic_abstract": True}


class Left_Back(Moderately_Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'LB'
    }


class Right_Back(Moderately_Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'RB'
    }


class Defensive_Midfielder(Moderately_Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'DM'
    }


class Full_Back(Moderately_Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'FB'
    }


class Central_Midfielder(Player):
    __tablename__ = 'central_midfielders'

    id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
    central_midfielder_name: Mapped[str] = mapped_column(key='player.name')
    shots: Mapped[int]
    shots_on_target: Mapped[int]
    shots_on_target_percentage: Mapped[float]
    average_shot_distance: Mapped[int]
    xG: Mapped[float]
    non_penalty_xG: Mapped[float]
    goals_minus_xG: Mapped[float]
    passes: Mapped[int]
    passes_completion: Mapped[float]
    total_passing_dist: Mapped[int]
    progressive_passing_disc: Mapped[int]
    short_passes: Mapped[int]
    short_passes_completion: Mapped[float]
    medium_passes: Mapped[int]
    medium_passes_completion: Mapped[float]
    long_passes: Mapped[int]
    long_passes_completion: Mapped[float]
    progressive_passes: Mapped[int]
    passes_att_3rd: Mapped[int]
    carries_into_penalty_area: Mapped[int]
    key_passes: Mapped[int]
    crosses_penalty_area: Mapped[int]
    through_passees: Mapped[int]
    switches: Mapped[int]
    crosses: Mapped[int]
    tackles: Mapped[int]
    tackles_won: Mapped[int]
    tackles_def_3rd: Mapped[int]
    tackles_mid_3rd: Mapped[int]
    tackles_att_3rd: Mapped[int]
    dribblers_tackles_won: Mapped[int]
    dribblers_tackles_attemped: Mapped[int]
    dribblers_tackles_won_percentage: Mapped[float]
    blocks: Mapped[int]
    shots_blocks: Mapped[int]
    passes_blocks: Mapped[int]
    interceptions: Mapped[int]
    errors: Mapped[int]
    clearances: Mapped[int]
    fouls: Mapped[int]
    recoveries: Mapped[int]
    air_duels_won: Mapped[int]
    air_duels_won_percentage: Mapped[float]
    shot_creating_actions: Mapped[int]
    goal_creating_actions: Mapped[int]
    gca_ball_live: Mapped[int]
    gca_ball_dead: Mapped[int]

    __mapper_args__ = {
        "polymorphic_identity": "CM"
    }


class Attacking(Player):
    __tablename__ = 'attackings'
    id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
    attacking_player_name: Mapped[str] = mapped_column(key='player.name')

    shots: Mapped[int]
    shots_on_target: Mapped[int]
    shots_on_target_percentage: Mapped[float]
    average_shot_distance: Mapped[int]
    xG: Mapped[float]
    non_penalty_xG: Mapped[float]
    penalty_made: Mapped[int]
    penalty_attempted: Mapped[int]
    goals_minus_xG: Mapped[float]
    passes: Mapped[int]
    passes_completion: Mapped[float]
    total_passing_dist: Mapped[int]
    progressive_passing_disc: Mapped[int]
    short_passes: Mapped[int]
    short_passes_completion: Mapped[float]
    medium_passes: Mapped[int]
    medium_passes_completion: Mapped[float]
    long_passes: Mapped[int]
    long_passes_completion: Mapped[float]
    progressive_passes: Mapped[int]
    passes_att_3rd: Mapped[int]
    carries_into_penalty_area: Mapped[int]
    key_passes: Mapped[int]
    crosses_penalty_area: Mapped[int]
    through_passees: Mapped[int]
    switches: Mapped[int]
    crosses: Mapped[int]
    air_duels_won: Mapped[int]
    air_duels_won_percentage: Mapped[float]
    recoveries: Mapped[int]
    shot_creating_actions: Mapped[int]
    goal_creating_actions: Mapped[int]
    gca_ball_live: Mapped[int]
    gca_ball_dead: Mapped[int]
    sca_take_on: Mapped[int]
    sca_shots: Mapped[int]
    sca_fouls_drawn: Mapped[int]
    gca_take_on: Mapped[int]
    gca_shots: Mapped[int]
    gca_fouls_drawn: Mapped[int]

    __mapper_args__ = {"polymorphic_abstract": True}


class Attacking_Midfielder(Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'AM'
    }


class Left_Midfielder(Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'LM'
    }


class Right_Midfielder(Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'RM'
    }


class Left_Winger(Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'LW'
    }


class Right_Winger(Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'RW'
    }


class Wide_Midfielder(Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'WM'
    }


class Forward(Attacking):

    __mapper_args__ = {
        "polymorphic_identity": 'FW'
    }
