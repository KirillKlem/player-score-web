def count_stat(players, stat, minutes=False, matches=False):
  counter = test_counter(minutes, matches)          #Проверяем считаем мы относительно минут или матчей

  avg_player_stat = 0
  player_stat = list()

  for player in players:
      avg_player_stat += (player[stat] / player[counter]) #Считаем сумму показателя всех игроков с расчётом деления на матчи/минуты
      player_stat.append({                #Записываем в список словарь игрока с ключами name и stat
        'name':player['name'], 
        stat:round((player[stat] / player[counter]), 2),#Округляем до двух знаков значение
      })
  avg_player_stat /= len(players)               #Получаем итоговое avg, деля на кол-во игроков

  final_stats = {                       #Создаём для удобства чтения отдельную переменную с финальными данными
    'avg_stat':round(avg_player_stat, 2),          #Округляем до двух знаков значение
    'player_stat':player_stat,
  } 

  return final_stats

 
def test_counter(minutes=False, matches=False):         #Проверка на счёт относительно минут или матчей *уже сомнения по поводу целесообразности минут и функции соответственно*
  try:
    if minutes == True and matches == False:        #Условия для минут
      return 'minutes'        
    elif matches == True and minutes == False:       #Условия для матчей
      return 'matches'
    else:  
      raise KeyError                   #Если не названо ни одно значение как True или оба являются True, то вызываем ошибку
  except(KeyError):                      #Обрабатываем эту ошибку
    print('The counter is not set, the "matches" are set by default')  #Сообщаем пользователю об неверном указании для делителя 
    return 'matches'                          #Устанавливаем матчи по умолчанию
  
def get_percentage(players, stat, minutes=False, matches=False):
  counter = test_counter(minutes, matches)             #Проверка для делителя

  for player in players:
    player[stat] /= player[counter]               #Считаем stat относительно минут/матчей

  sorted_players = sorted(players, key=lambda x: x[stat])     #Сортировка по stat

  percentages = {}                         #Итоговый словарь для скора
  for player in sorted_players:                                       #Добавляем каждого игрока в наш словарь для скора
    percentages[player['name']] = {                                    #Ключом будет являться имя игрока для удобства вызова
      'percentage':round(100.01 - ((sorted_players.index(player) + 1) / len(sorted_players) * 100), 2), #Нахождение в какой процент лучших входит игрок, с округлением до двух знаков после запятой *вопрос по 0.01*
      'positive_score':round(((sorted_players.index(player) + 1) / len(sorted_players) * 100), 2),   #Нахождение скора для позитивного показателя (проценты - скор для негативного показателя)
      }                                        
    
  return percentages 