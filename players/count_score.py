from main.extensions import db
from .models import Player
from .utils import attribute_names
from . import constants

from pprint import pprint
  
def get_percentage(players: dict[str, dict], stat: str, positive_stat=None) -> dict[str, dict]:    
    '''
    We count the score for one characteristic (stat) of the selected players (players)
    We get a score for each player: name -> dict
    The dict consists of two characteristics:
    negative_score is responsible for the characteristics that reflect the negative influence of the player
    positive_score is responsible for the characteristics that reflect the positive influence of the player
    '''     

    for player in players:
        if stat[-2:] != '90':
            player[stat] /= (player['playing_time_min'] / 90)       

    ranked_players = sorted(players, key=lambda x: x[stat])    

    percentages = {}                       
    for player in ranked_players:    
        player_score = (ranked_players.index(player) + 1) / len(ranked_players) * 100   

        if positive_stat is True:
            percentages[player['name']] = {'original_score':round(player_score, 2)}  
        elif positive_stat is False:
            percentages[player['name']] = {'original_score':round((100.01 - player_score), 2)}                          
        else:
            raise KeyError('It is unknown which characteristic: positive or negative')
                                           
        
    return percentages 


def get_names(position: str) -> list[str]:
    '''
    We get from DB the names of all players of a certain position (position)
    '''
    
    players = db.session.execute(db.select(Player).filter_by(pos=position)).scalars()
    player_names = []
    for player in players:
        if player.playing_time_min > 600:
            player_names.append(player.name)

    return player_names


def create_players(player_names: list[str]) -> list[Player]:
   '''
   We get models suitable for the transmitted players (player_names)
   '''
   
   player_models = []
   for player_name in player_names:
        player_models.append(Player.query.filter_by(name=player_name).first())

   return player_models  

  
def get_all_stats(player_names: list[str]) -> list[dict]:
    '''
    We get all the statistics for the specified players (player_names) from DB
    The resulting value is in the form: player name -> dict from the data
    '''

    player_models = create_players(player_names)
    players = []

    for player in player_models:
        stats = {}
        for attribute in attribute_names(type(player)):
            stats[attribute] = getattr(player, attribute)
        players.append(stats)
    
    return players


def count_score_of_stat(players: list[dict], const: dict):
    '''
    We calculate the score of players for each characteristic from a constant (const) containing the necessary fields
    '''

    score_of_types = {}

    for type in const:
        if type in constants.NEGATIVE_PLAYER_STATS:
            score_of_types[type] = get_percentage(players, type, positive_stat=False)
        else:
            score_of_types[type] = get_percentage(players, type, positive_stat=True)
    
    return score_of_types


def create_weighted_average(player_names: list[str], player_stats: list[dict], const: dict) -> dict[str, dict]:
    '''
    Creating a dictionary for the specified players (player_names), in which the weighted average value is calculated
    '''

    player_stats = count_score_of_stat(player_stats, const)
    weighted_average_stats = {player: {} for player in player_names}

    for player_name in player_names:
        weighted_average_stats[player_name] = count_weighted_average(player_name, player_stats, const, addition='original_score', type_name=True)

    
    return weighted_average_stats

def count_weighted_average(player_name: str, player_stats: dict[str, dict], const: dict, addition=None, type_name=False, name_type=False) -> dict:
    '''
    Count weighted average for the specified players (player_names) 
    The weight is taken from the needful constant (const)
    Player stats (player_stats) contains data about players
    Note:
    "addition" is created for data structures that are longer than expected
    "type_name" or "name_type" indicate a particular data structure
    "type_name" means that "player_stats" stores data in the form: type -> name
    "name_type" means that "player_stats" stores data in the form: name -> type

    Rough formula for calculating the weighted average:
    (value1 * its_weight + value2 * its_weight ... valueN * its_weight) / (sum of all weights)
    '''
    
    player_score_weight = 0
    player_score = 0
    for type in const:
        player_score_weight += const[type]
        if addition:
            player_score += player_stats[type.lower()][player_name][addition] * const[type]
        else:
            if type_name:
                player_score += player_stats[type.lower()][player_name] * const[type]
            elif name_type:
                player_score += player_stats[player_name][type.lower()] * const[type]
            else:
                raise KeyError('The data structure is not defined')

    try:
        return round((player_score / player_score_weight), 2)
    except ZeroDivisionError:
        raise ValueError('Weights of all stats are zero, you have to specify its')


    

    
def count_main_weighted_average(player_names: list[str], weighted_average_stats: dict[str, dict], const: dict) -> dict[str, float]:
    '''
    Create a dict with weighted averages for the main constant (const)
    Data in the resulting dictionary: player name -> weighted average
    '''
    
    result_score = {}

    for player_name in player_names:
        result_score[player_name] = count_weighted_average(player_name, weighted_average_stats, const, type_name=True)

    return result_score



def add_to_all_score(all_weighted_average: dict[str, dict], all_score: dict[str, dict]):
    '''
    Add (all) intermediate values for a complete list of values
    '''

    for type in all_weighted_average:
        for player_name, value in all_weighted_average[type].items():
            all_score[player_name][type] = value


def add_to_final_score(type_name: str, intermediate_score: dict[str, float], final_score: dict[str, dict]):
    '''
    Add (main) intermediate values for a complete list of values
    '''

    for player in final_score:
        final_score[player][type_name] = intermediate_score[player]

  
def count_total_score(final_score: dict[str, dict], const: str):
    '''
    Count total score of each player and add its in "final score" as 'total'
    '''
    
    for player_name in final_score:
        final_score[player_name]['total'] = count_weighted_average(player_name, final_score, const, name_type=True)


