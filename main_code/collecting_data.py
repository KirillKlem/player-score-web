import soccerdata as sd
from pathlib import Path
import os

basedir = os.path.abspath(os.path.dirname(__file__))

fbref = sd.FBref(leagues='ENG-Premier League', seasons='22-23', proxy=None,
                 no_cache=False, no_store=True, data_dir=Path(os.path.join(basedir, 'data')))

players = fbref.read_player_season_stats(stat_type='standard')
players_json = players.to_json(orient='index')
