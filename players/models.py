from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from main.extensions import db


class Player(db.Model):
    __tablename__ = 'player'

    id: Mapped[int] = Column(Integer, primary_key=True)
    a_minus_xag: Mapped[float] = Column(Float, nullable=True)
    age: Mapped[int] = Column(Integer, nullable=True)
    ast: Mapped[int] = Column(Integer, nullable=True)
    att: Mapped[int] = Column(Integer, nullable=True)
    carries_1_in_3: Mapped[int] = Column(Integer, nullable=True)
    carries_carries: Mapped[int] = Column(Integer, nullable=True)
    carries_cpa: Mapped[int] = Column(Integer, nullable=True)
    carries_dis: Mapped[int] = Column(Integer, nullable=True)
    carries_mis: Mapped[int] = Column(Integer, nullable=True)
    carries_prgc: Mapped[int] = Column(Integer, nullable=True)
    carries_prgdist: Mapped[int] = Column(Integer, nullable=True)
    carries_totdist: Mapped[int] = Column(Integer, nullable=True)
    corner_kicks_in: Mapped[int] = Column(Integer, nullable=True)
    corner_kicks_out: Mapped[int] = Column(Integer, nullable=True)
    corner_kicks_str: Mapped[int] = Column(Integer, nullable=True)
    crspa: Mapped[int] = Column(Integer, nullable=True)
    expected_npxg_plus_xag: Mapped[float] = Column(Float, nullable=True)
    expected_npxg: Mapped[float] = Column(Float, nullable=True)
    expected_xag: Mapped[float] = Column(Float, nullable=True)
    expected_xg: Mapped[float] = Column(Float, nullable=True)
    kp: Mapped[int] = Column(Integer, nullable=True)
    long_att: Mapped[int] = Column(Integer, nullable=True)
    long_cmp_percent: Mapped[float] = Column(Float, nullable=True)
    long_cmp: Mapped[int] = Column(Integer, nullable=True)
    medium_att: Mapped[int] = Column(Integer, nullable=True)
    medium_cmp_percent: Mapped[float] = Column(Float, nullable=True)
    medium_cmp: Mapped[int] = Column(Integer, nullable=True)
    name: Mapped[str]
    nation: Mapped[str]
    on1_in_3: Mapped[int] = Column(Integer, nullable=True)
    on90s: Mapped[float] = Column(Float, nullable=True)
    outcomes_blocks: Mapped[int] = Column(Integer, nullable=True)
    outcomes_cmp: Mapped[int] = Column(Integer, nullable=True)
    outcomes_off: Mapped[int] = Column(Integer, nullable=True)
    pass_types_ck: Mapped[int] = Column(Integer, nullable=True)
    pass_types_crs: Mapped[int] = Column(Integer, nullable=True)
    pass_types_dead: Mapped[int] = Column(Integer, nullable=True)
    pass_types_fk: Mapped[int] = Column(Integer, nullable=True)
    pass_types_live: Mapped[int] = Column(Integer, nullable=True)
    pass_types_sw: Mapped[int] = Column(Integer, nullable=True)
    pass_types_tb: Mapped[int] = Column(Integer, nullable=True)
    pass_types_ti: Mapped[int] = Column(Integer, nullable=True)
    per_90_minutes_ast: Mapped[float] = Column(Float, nullable=True)
    per_90_minutes_g_minus_pk: Mapped[float] = Column(Float, nullable=True)
    per_90_minutes_g_plus_a_minus_pk: Mapped[float] = Column(Float, nullable=True)
    per_90_minutes_g_plus_a: Mapped[float] = Column(Float, nullable=True)
    per_90_minutes_gls: Mapped[float] = Column(Float, nullable=True)
    per_90_minutes_npxg_plus_xag: Mapped[float] = Column(Float, nullable=True)
    per_90_minutes_npxg: Mapped[float] = Column(Float, nullable=True)
    per_90_minutes_xag: Mapped[float] = Column(Float, nullable=True)
    per_90_minutes_xg_plus_xag: Mapped[float] = Column(Float, nullable=True)
    per_90_minutes_xg: Mapped[float] = Column(Float, nullable=True)
    performance_ast: Mapped[int] = Column(Integer, nullable=True)
    performance_crdr: Mapped[int] = Column(Integer, nullable=True)
    performance_crdy: Mapped[int] = Column(Integer, nullable=True)
    performance_g_minus_pk: Mapped[int] = Column(Integer, nullable=True)
    performance_g_plus_a: Mapped[int] = Column(Integer, nullable=True)
    performance_gls: Mapped[int] = Column(Integer, nullable=True)
    performance_pk: Mapped[int] = Column(Integer, nullable=True)
    performance_pkatt: Mapped[int] = Column(Integer, nullable=True)
    playing_time_90s: Mapped[float] = Column(Float, nullable=True)
    playing_time_min_percent: Mapped[float] = Column(Float, nullable=True)
    playing_time_min: Mapped[int] = Column(Integer, nullable=True)
    playing_time_mn_in_mp: Mapped[int] = Column(Integer, nullable=True)
    playing_time_mp: Mapped[int] = Column(Integer, nullable=True)
    playing_time_starts: Mapped[int] = Column(Integer, nullable=True)
    pos: Mapped[str] = mapped_column()
    ppa: Mapped[int] = Column(Integer, nullable=True)
    prgp: Mapped[int] = Column(Integer, nullable=True)
    progression_prgc: Mapped[int] = Column(Integer, nullable=True)
    progression_prgp: Mapped[int] = Column(Integer, nullable=True)
    progression_prgr: Mapped[int] = Column(Integer, nullable=True)
    receiving_prgr: Mapped[int] = Column(Integer, nullable=True)
    receiving_rec: Mapped[int] = Column(Integer, nullable=True)
    short_att: Mapped[int] = Column(Integer, nullable=True)
    short_cmp_percent: Mapped[float] = Column(Float, nullable=True)
    short_cmp: Mapped[int] = Column(Integer, nullable=True)
    starts_compl: Mapped[int] = Column(Integer, nullable=True)
    starts_mn_in_start: Mapped[int] = Column(Integer, nullable=True)
    starts_starts: Mapped[int] = Column(Integer, nullable=True)
    subs_mn_in_sub: Mapped[int] = Column(Integer, nullable=True)
    subs_subs: Mapped[int] = Column(Integer, nullable=True)
    subs_unsub: Mapped[int] = Column(Integer, nullable=True)
    take_minus_ons_att: Mapped[int] = Column(Integer, nullable=True)
    take_minus_ons_succ_percent: Mapped[float] = Column(Float, nullable=True)
    take_minus_ons_succ: Mapped[int] = Column(Integer, nullable=True)
    take_minus_ons_tkld_percent: Mapped[float] = Column(Float, nullable=True)
    take_minus_ons_tkld: Mapped[int] = Column(Integer, nullable=True)
    team_success_plus_in_minus: Mapped[int] = Column(Integer, nullable=True)
    team_success_plus_in_minus_90: Mapped[float] = Column(Float, nullable=True)
    team_success_on_minus_off: Mapped[float] = Column(Float, nullable=True)
    team_success_ong: Mapped[int] = Column(Integer, nullable=True)
    team_success_onga: Mapped[int] = Column(Integer, nullable=True)
    team_success_ppm: Mapped[float] = Column(Float, nullable=True)
    team_success_xg_on_minus_off: Mapped[float] = Column(Float, nullable=True)
    team_success_xg_onxg: Mapped[float] = Column(Float, nullable=True)
    team_success_xg_onxga: Mapped[float] = Column(Float, nullable=True)
    team_success_xg_xg_plus_in_minus: Mapped[float] = Column(Float, nullable=True)
    team_success_xg_xg_plus_in_minus_90: Mapped[float] = Column(Float, nullable=True)
    team: Mapped[str]
    total_att: Mapped[int] = Column(Integer, nullable=True)
    total_cmp_percent: Mapped[float] = Column(Float, nullable=True)
    total_cmp: Mapped[int] = Column(Integer, nullable=True)
    total_prgdist: Mapped[int] = Column(Integer, nullable=True)
    total_totdist: Mapped[int] = Column(Integer, nullable=True)
    touches_att_3rd: Mapped[int] = Column(Integer, nullable=True)
    touches_att_pen: Mapped[int] = Column(Integer, nullable=True)
    touches_def_3rd: Mapped[int] = Column(Integer, nullable=True)
    touches_def_pen: Mapped[int] = Column(Integer, nullable=True)
    touches_live: Mapped[int] = Column(Integer, nullable=True)
    touches_mid_3rd: Mapped[int] = Column(Integer, nullable=True)
    touches_touches: Mapped[int] = Column(Integer, nullable=True)
    xa: Mapped[float] = Column(Float, nullable=True)
    xag: Mapped[float] = Column(Float, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "player",
        "polymorphic_on": pos
    }

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


class Goalkeeper(Player):
    __tablename__ = 'goalkeeper'

    id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
    crosses_opp: Mapped[int] = Column(Integer, nullable=True)
    crosses_stp_percent: Mapped[float] = Column(Float, nullable=True)
    crosses_stp: Mapped[int] = Column(Integer, nullable=True)
    expected_in_90: Mapped[float] = Column(Float, nullable=True)
    expected_psxg_in_sot: Mapped[float] = Column(Float, nullable=True)
    expected_psxg_plus_in_minus: Mapped[float] = Column(Float, nullable=True)
    expected_psxg: Mapped[float] = Column(Float, nullable=True)
    goal_kicks_att: Mapped[int] = Column(Integer, nullable=True)
    goal_kicks_avglen: Mapped[float] = Column(Float, nullable=True)
    goal_kicks_launch_percent: Mapped[float] = Column(Float, nullable=True)
    goals_ck: Mapped[int] = Column(Integer, nullable=True)
    goals_fk: Mapped[int] = Column(Integer, nullable=True)
    goals_ga: Mapped[int] = Column(Integer, nullable=True)
    goals_og: Mapped[int] = Column(Integer, nullable=True)
    goals_pka: Mapped[int] = Column(Integer, nullable=True)
    launched_att: Mapped[int] = Column(Integer, nullable=True)
    launched_cmp_percent: Mapped[float] = Column(Float, nullable=True)
    launched_cmp: Mapped[int] = Column(Integer, nullable=True)
    passes_att: Mapped[int] = Column(Integer, nullable=True)
    passes_avglen: Mapped[float] = Column(Float, nullable=True)
    passes_launch_percent: Mapped[float] = Column(Float, nullable=True)
    passes_thr: Mapped[int] = Column(Integer, nullable=True)
    penalty_kicks_pka: Mapped[int] = Column(Integer, nullable=True)
    penalty_kicks_pkatt: Mapped[int] = Column(Integer, nullable=True)
    penalty_kicks_pkm: Mapped[int] = Column(Integer, nullable=True)
    penalty_kicks_pksv: Mapped[int] = Column(Integer, nullable=True)
    penalty_kicks_save_percent: Mapped[float] = Column(Float, nullable=True)
    performance_cs_percent: Mapped[float] = Column(Float, nullable=True)
    performance_cs: Mapped[int] = Column(Integer, nullable=True)
    performance_d: Mapped[int] = Column(Integer, nullable=True)
    performance_ga: Mapped[int] = Column(Integer, nullable=True)
    performance_ga90: Mapped[float] = Column(Float, nullable=True)
    performance_l: Mapped[int] = Column(Integer, nullable=True)
    performance_save_percent: Mapped[float] = Column(Float, nullable=True)
    performance_saves: Mapped[int] = Column(Integer, nullable=True)
    performance_sota: Mapped[int] = Column(Integer, nullable=True)
    performance_w: Mapped[int] = Column(Integer, nullable=True)
    sweeper_opa_in_90: Mapped[float] = Column(Float, nullable=True)
    sweeper_opa: Mapped[int] = Column(Integer, nullable=True)
    sweeper_avgdist: Mapped[float] = Column(Float, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "GK"
    }


class Defender(Player):
    __tablename__ = 'defender'

    id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
    aerial_duels_lost: Mapped[int] = Column(Integer, nullable=True)
    aerial_duels_won_percent: Mapped[float] = Column(Float, nullable=True)
    aerial_duels_won: Mapped[int] = Column(Integer, nullable=True)
    blocks_blocks: Mapped[int] = Column(Integer, nullable=True)
    blocks_pass: Mapped[int] = Column(Integer, nullable=True)
    blocks_sh: Mapped[int] = Column(Integer, nullable=True)
    challenges_att: Mapped[int] = Column(Integer, nullable=True)
    challenges_lost: Mapped[int] = Column(Integer, nullable=True)
    challenges_tkl_percent: Mapped[float] = Column(Float, nullable=True)
    challenges_tkl: Mapped[int] = Column(Integer, nullable=True)
    clr: Mapped[int] = Column(Integer, nullable=True)
    err: Mapped[int] = Column(Integer, nullable=True)
    int_: Mapped[int] = Column(Integer, nullable=True)
    performance_2crdy: Mapped[int] = Column(Integer, nullable=True)
    performance_crs: Mapped[int] = Column(Integer, nullable=True)
    performance_fld: Mapped[int] = Column(Integer, nullable=True)
    performance_fls: Mapped[int] = Column(Integer, nullable=True)
    performance_int: Mapped[int] = Column(Integer, nullable=True)
    performance_off: Mapped[int] = Column(Integer, nullable=True)
    performance_og: Mapped[int] = Column(Integer, nullable=True)
    performance_pkcon: Mapped[int] = Column(Integer, nullable=True)
    performance_pkwon: Mapped[int] = Column(Integer, nullable=True)
    performance_recov: Mapped[int] = Column(Integer, nullable=True)
    performance_tklw: Mapped[int] = Column(Integer, nullable=True)
    tackles_att_3rd: Mapped[int] = Column(Integer, nullable=True)
    tackles_def_3rd: Mapped[int] = Column(Integer, nullable=True)
    tackles_mid_3rd: Mapped[int] = Column(Integer, nullable=True)
    tackles_tkl: Mapped[int] = Column(Integer, nullable=True)
    tackles_tklw: Mapped[int] = Column(Integer, nullable=True)
    tkl_plus_int: Mapped[int] = Column(Integer, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "DF"
    }


class Midfielder(Player):
    __tablename__ = 'midfielder'

    id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
    aerial_duels_lost: Mapped[int] = Column(Integer, nullable=True)
    aerial_duels_won_percent: Mapped[float] = Column(Float, nullable=True)
    aerial_duels_won: Mapped[int] = Column(Integer, nullable=True)
    blocks_blocks: Mapped[int] = Column(Integer, nullable=True)
    blocks_pass: Mapped[int] = Column(Integer, nullable=True)
    blocks_sh: Mapped[int] = Column(Integer, nullable=True)
    challenges_att: Mapped[int] = Column(Integer, nullable=True)
    challenges_lost: Mapped[int] = Column(Integer, nullable=True)
    challenges_tkl_percent: Mapped[float] = Column(Float, nullable=True)
    challenges_tkl: Mapped[int] = Column(Integer, nullable=True)
    clr: Mapped[int] = Column(Integer, nullable=True)
    err: Mapped[int] = Column(Integer, nullable=True)
    expected_g_minus_xg: Mapped[float] = Column(Float, nullable=True)
    expected_np_g_minus_xg: Mapped[float] = Column(Float, nullable=True)
    expected_npxg_in_sh: Mapped[float] = Column(Float, nullable=True)
    gca_gca: Mapped[int] = Column(Integer, nullable=True)
    gca_gca90: Mapped[float] = Column(Float, nullable=True)
    gca_types_def: Mapped[int] = Column(Integer, nullable=True)
    gca_types_fld: Mapped[int] = Column(Integer, nullable=True)
    gca_types_passdead: Mapped[int] = Column(Integer, nullable=True)
    gca_types_passlive: Mapped[int] = Column(Integer, nullable=True)
    gca_types_sh: Mapped[int] = Column(Integer, nullable=True)
    gca_types_to: Mapped[int] = Column(Integer, nullable=True)
    int_: Mapped[int] = Column(Integer, nullable=True)
    performance_2crdy: Mapped[int] = Column(Integer, nullable=True)
    performance_crs: Mapped[int] = Column(Integer, nullable=True)
    performance_fld: Mapped[int] = Column(Integer, nullable=True)
    performance_fls: Mapped[int] = Column(Integer, nullable=True)
    performance_int: Mapped[int] = Column(Integer, nullable=True)
    performance_off: Mapped[int] = Column(Integer, nullable=True)
    performance_og: Mapped[int] = Column(Integer, nullable=True)
    performance_pkcon: Mapped[int] = Column(Integer, nullable=True)
    performance_pkwon: Mapped[int] = Column(Integer, nullable=True)
    performance_recov: Mapped[int] = Column(Integer, nullable=True)
    performance_tklw: Mapped[int] = Column(Integer, nullable=True)
    sca_sca: Mapped[int] = Column(Integer, nullable=True)
    sca_sca90: Mapped[float] = Column(Float, nullable=True)
    sca_types_def: Mapped[int] = Column(Integer, nullable=True)
    sca_types_fld: Mapped[int] = Column(Integer, nullable=True)
    sca_types_passdead: Mapped[int] = Column(Integer, nullable=True)
    sca_types_passlive: Mapped[int] = Column(Integer, nullable=True)
    sca_types_sh: Mapped[int] = Column(Integer, nullable=True)
    sca_types_to: Mapped[int] = Column(Integer, nullable=True)
    standard_dist: Mapped[float] = Column(Float, nullable=True)
    standard_fk: Mapped[int] = Column(Integer, nullable=True)
    standard_g_in_sh: Mapped[float] = Column(Float, nullable=True)
    standard_g_in_sot: Mapped[float] = Column(Float, nullable=True)
    standard_gls: Mapped[int] = Column(Integer, nullable=True)
    standard_pk: Mapped[int] = Column(Integer, nullable=True)
    standard_pkatt: Mapped[int] = Column(Integer, nullable=True)
    standard_sh_in_90: Mapped[float] = Column(Float, nullable=True)
    standard_sh: Mapped[int] = Column(Integer, nullable=True)
    standard_sot_in_90: Mapped[float] = Column(Float, nullable=True)
    standard_sot_percent: Mapped[float] = Column(Float, nullable=True)
    standard_sot: Mapped[int] = Column(Integer, nullable=True)
    tackles_att_3rd: Mapped[int] = Column(Integer, nullable=True)
    tackles_def_3rd: Mapped[int] = Column(Integer, nullable=True)
    tackles_mid_3rd: Mapped[int] = Column(Integer, nullable=True)
    tackles_tkl: Mapped[int] = Column(Integer, nullable=True)
    tackles_tklw: Mapped[int] = Column(Integer, nullable=True)
    tkl_plus_int: Mapped[int] = Column(Integer, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "MF"
    }


class Attacking(Player):
    __tablename__ = 'attacking'

    id: Mapped[int] = mapped_column(ForeignKey("player.id"), primary_key=True)
    expected_g_minus_xg: Mapped[float] = Column(Float, nullable=True)
    expected_np_g_minus_xg: Mapped[float] = Column(Float, nullable=True)
    expected_npxg_in_sh: Mapped[float] = Column(Float, nullable=True)
    gca_gca: Mapped[int] = Column(Integer, nullable=True)
    gca_gca90: Mapped[float] = Column(Float, nullable=True)
    gca_types_def: Mapped[int] = Column(Integer, nullable=True)
    gca_types_fld: Mapped[int] = Column(Integer, nullable=True)
    gca_types_passdead: Mapped[int] = Column(Integer, nullable=True)
    gca_types_passlive: Mapped[int] = Column(Integer, nullable=True)
    gca_types_sh: Mapped[int] = Column(Integer, nullable=True)
    gca_types_to: Mapped[int] = Column(Integer, nullable=True)
    sca_sca: Mapped[int] = Column(Integer, nullable=True)
    sca_sca90: Mapped[float] = Column(Float, nullable=True)
    sca_types_def: Mapped[int] = Column(Integer, nullable=True)
    sca_types_fld: Mapped[int] = Column(Integer, nullable=True)
    sca_types_passdead: Mapped[int] = Column(Integer, nullable=True)
    sca_types_passlive: Mapped[int] = Column(Integer, nullable=True)
    sca_types_sh: Mapped[int] = Column(Integer, nullable=True)
    sca_types_to: Mapped[int] = Column(Integer, nullable=True)
    standard_dist: Mapped[float] = Column(Float, nullable=True)
    standard_fk: Mapped[int] = Column(Integer, nullable=True)
    standard_g_in_sh: Mapped[float] = Column(Float, nullable=True)
    standard_g_in_sot: Mapped[float] = Column(Float, nullable=True)
    standard_gls: Mapped[int] = Column(Integer, nullable=True)
    standard_pk: Mapped[int] = Column(Integer, nullable=True)
    standard_pkatt: Mapped[int] = Column(Integer, nullable=True)
    standard_sh_in_90: Mapped[float] = Column(Float, nullable=True)
    standard_sh: Mapped[int] = Column(Integer, nullable=True)
    standard_sot_in_90: Mapped[float] = Column(Float, nullable=True)
    standard_sot_percent: Mapped[float] = Column(Float, nullable=True)
    standard_sot: Mapped[int] = Column(Integer, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": 'FW'
    }