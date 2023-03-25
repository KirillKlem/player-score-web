import soccerdata as sd

fbref = sd.FBref(leagues='ENG-Premier League', seasons='22-23', no_store=True)

players = fbref.read_player_season_stats(stat_type='standard')
players_json = players.to_json(orient='index')
