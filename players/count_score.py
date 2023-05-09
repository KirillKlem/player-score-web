from main.extensions import db
from .models import Player
from .utils import attribute_names

from typing import *
from pprint import pprint

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
 
  
def get_percentage(players: dict[str, dict], stat: str) -> dict[str, dict]:    
    '''
    Считаем скор для одной характеристики (stat) выбранных игроков (players)
    Получаем скор по каждому игроку: имя -> словарь 
    Словарь состоит из двух характеристик: 
    negative_score отвечает за характеристики, которые отражают негативное влияние игрока
    positive_score отвечает за характеристики, которые отражают положительное влияние игрока
    '''     

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


def get_names(position: str) -> list[str]:
    '''
    Получаем из ДБ имена всех игроков определённой позиции (position)
    '''
    
    players = db.session.execute(db.select(Player).filter_by(pos=position)).scalars()
    player_names = []
    for player in players:
        player_names.append(player.name)

    return player_names


def create_players(player_names: list[str]) -> list[Player]:
   '''
   Получаем модели, подходящие для передаваемых игроков (player_names) 
   '''
   
   player_models = []
   for player_name in player_names:
        player_models.append(Player.query.filter_by(name=player_name).first())

   return player_models  

  
def get_all_stats(player_names: list[str]) -> list[dict]:
    '''
    Получаем всю статистику по указанным игрокам (player_names) из ДБ
    Получаемое значение в виде: имя_игрока -> словарь из данных
    '''

    player_models = create_players(player_names)
    players = []

    for player in player_models:
        stats = {}
        for attribute in attribute_names(type(player)):
            stats[attribute] = getattr(player, attribute)
        players.append(stats)
    
    return players


def get_type_of_stats(players: list[dict], const: dict):
    '''
    Рассчитываем скор игроков по каждой характеристике из константы (const), содержащей нужные поля
    '''

    score_of_types = {}

    for type in const:
        score_of_types[type] = get_percentage(players, type)
    
    return score_of_types


def create_weighted_average(player_names: list[str], player_stats: list[dict], const: dict) -> dict[str, float]:
    '''
    Создаём словарь для указанных игроков (player_names), в котором посчитано средневзвешенное значение
    '''

    player_stats = get_type_of_stats(player_stats, const)
    weighted_average_stats = {player: {} for player in player_names}

    for player_name in player_names:
        weighted_average_stats[player_name] = count_weighted_average(player_name, player_stats, const, 'positive_score')

    
    return weighted_average_stats

def count_weighted_average(player_name: str, player_stats: float, type_names: dict, addition=None) -> dict:
    '''
    pass
    '''
    
    player_score_weight = 0
    player_score = 0
    for type in type_names:
        if addition:
            player_score_weight += type_names[type]
            player_score += player_stats[type.lower()][player_name][addition] * type_names[type]
        else:
            player_score_weight += type_names[type]
            player_score += player_stats[type.lower()][player_name] * type_names[type]

    return round((player_score / player_score_weight), 2)


    

    
def count_score_of_types(player_names: list[str], weighted_average_stats: dict[str, float], const: dict) -> dict[str, float]:
    result_score = {}

    for player_name in player_names:
        result_score[player_name] = count_weighted_average(player_name, weighted_average_stats, const)

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


