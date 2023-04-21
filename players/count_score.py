from main.extensions import db
from .models import Player

def count_stat(players, stat):      

  avg_player_stat = 0
  player_stats = list()

  for player in players:
      current_player_stat = player[stat] / (player['playing_time_min'] / 90)
      avg_player_stat += current_player_stat
      player_stats.append({                
        'name':player['name'], 
        stat:round(current_player_stat, 2),
      })
  avg_player_stat /= len(players)              

  final_stats = {                       
    'avg_stat':round(avg_player_stat, 2),          
    'player_stat':player_stats,
  } 

  return final_stats
 
  
def get_percentage(players, stat):         

  for player in players:
    player[stat] /= (player['playing_time_min'] / 90)       

  ranked_players = sorted(players, key=lambda x: x[stat])    

  percentages = {}                       
  for player in ranked_players:    
    player_score = (ranked_players.index(player) + 1) / len(ranked_players) * 100                                  
    percentages[player['name']] = {                                 
      'percentage':round((100.01 - player_score), 2),
      'positive_score':round(player_score, 2),   
      }                                        
    
  return percentages 


def get_name_players(position):
  player_names = []

  players = Player.query.filter(Player.pos == position).all()
  for player in players:
    player_names.append(player)
  return player_names
  
