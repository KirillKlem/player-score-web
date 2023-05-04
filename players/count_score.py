from main.extensions import db
from .models import Player
from .utils import attribute_names

def count_stat(players, stat):      

  avg_player_stat = 0
  player_stats = []

  for player in players:
      current_player_stat = getattr(player, stat) / (player.playing_time_min / 90)
      avg_player_stat += current_player_stat

      player_stats.append({                
        'name':player.name, 
        stat:round(current_player_stat, 2),
      })

  avg_player_stat /= len(players.all())          

  final_stats = {                       
    'avg_stat':round(avg_player_stat, 2),          
    'player_stat':player_stats,
  } 

  return final_stats
 
  
def get_percentage(players, stat):         

  for player in players:
    if stat[-2:] != '90':
        player[stat] /= (player['playing_time_min'] / 90)       

  ranked_players = sorted(players, key=lambda x: x[stat])    

  percentages = {}                       
  for player in ranked_players:    
    player_score = (ranked_players.index(player) + 1) / len(ranked_players) * 100   

    percentages[player['name']] = {                                 
      'negative_score':round((100.01 - player_score), 2),
      'positive_score':round(player_score, 2),   
      }                                        
    
  return percentages 


def get_names(position):
    players = db.session.execute(db.select(Player).filter_by(pos=position)).scalars()
    player_names = []
    for player in players:
        player_names.append(player.name)

    return player_names


def create_players(player_names):
   players = []
   for player_name in player_names:
        players.append(Player.query.filter_by(name=player_name).first())

   return players  

  
def get_all_stats(player_names):
    player_models = create_players(player_names)
    players = []

    for player in player_models:
        stats = {}
        for attribute in attribute_names(type(player)):
            stats[attribute] = getattr(player, attribute)
        players.append(stats)
    
    return players


def get_type_of_stats(players, const):
    score_of_types = {}

    for type in const:
        score_of_types[type] = get_percentage(players, type)
    
    return score_of_types


def count_weighted_average(score_of_types):
    for type, players in score_of_types.items():
        for player_name, player_stats in players.items():
            print(player_stats)


def count_score_of_types(player_names, score_of_types):
    result_score = {}

    for player in player_names:
        player_score_of_types = []

        for type in score_of_types:
            player_score_of_types.append(score_of_types[type][player]['positive_score']) 

        result_score[player] = round(sum(player_score_of_types) / len(player_score_of_types), 2)

    return result_score


def add_to_all_score(result_group_type, all_score):
    for player_name, value in result_group_type.items():
            all_score[player_name].append(value)


def add_to_final_score(adding_stat_name, final_score, all_score):
    for player in final_score:
        final_score[player][adding_stat_name] = round(sum(all_score[player]) / len(all_score[player]), 2)

  
def count_total_score(player_names, final_score, all_score):
    for player in player_names:

        total_score = []
        for stat in final_score[player]:
            total_score.append(final_score[player][stat])
        total_score = round(sum(total_score) / len(total_score), 2)

        final_score[player]['total'] = round(sum(all_score[player]) / len(all_score[player]), 2)


