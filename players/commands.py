from main.extensions import db
from .models import Player

import click

@click.command()
def print_gk():
    player_names = []

    players = db.session.execute(db.select(Player).filter_by(pos='GK')).scalars()
    for player in players:
        player_names.append(player)

    print(player_names)
    
# def possesion_gk(goalkeepers):
#   goalkeepers_posession_score = {}                            #Словарь скора каждого игрока
#   score_touches = get_percentage(goalkeepers, 'touches', matches=True)          #Получаем скор по touches
#   score_touches_def_pen = get_percentage(goalkeepers, 'touches_def_pen', matches=True)  #Получаем скор по touches_def_pen
#   score_touches_def_3rd = get_percentage(goalkeepers, 'touches_def_3rd', matches=True)  #Получаем скор по touches_def_3rd
#   score_touches_mid_3rd = get_percentage(goalkeepers, 'touches_mid_3rd', matches=True)  #Получаем скор по touches_mid_3rd

#   for gk in goalkeepers:
#     count = [score_touches[gk['name']]['positive_score'], score_touches_def_pen[gk['name']]['positive_score'],    #Вводим в список все значения скора для общего результата
#         score_touches_def_3rd[gk['name']]['positive_score'],score_touches_mid_3rd[gk['name']]['positive_score']] #*вопрос: как сократить функцию possesion_gk/что вынести в отдельную функцию*
#     count = sum(count) / len(count)           #Считаем средний скор как результат более общего показателя
#     goalkeepers_posession_score[gk['name']] = count   #Добавляем скор игрока по ключу его имени

#   return goalkeepers_posession_score

# def score_gk(goalkeepers):                                   #Тест-функция
#   gk_touches = count_stat(players=goalkeepers, stat='touches', matches=True)['player_stat'] #Получаем список словарей с ключами name и touches
#   avg_gk_touches = count_stat(players=goalkeepers, stat='touches', matches=True)['avg_stat'] #Получаем среднее число touches по игрокам
#   score_possesion_gk = possesion_gk(goalkeepers)

#   for gk in score_possesion_gk:
#     print(f"{gk}'s score = {score_possesion_gk[gk]}")        #Вывод каждого скора игрока по отдельности *вопрос: насколько это оптимально*
