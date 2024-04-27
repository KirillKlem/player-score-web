## Introduction
Hello! This is a web project that is experimental. Its essence is to calculate the rating of football players in the strongest leagues based on their performance.

## Requirements
* programming language Python3 and its libraries:
  + Web framework [Flask](https://flask.palletsprojects.com/en/3.0.x/)
  + Library for parsing data from the necessary sites [Soccrdata](https://soccerdata.readthedocs.io/en/latest/intro.html)
* sql toolkit [SQLAlchemy](https://www.sqlalchemy.org)

## Here's what was implemented
* Firstly, it was necessary to get data about football players, for this I used soccerdata, which provided data from the whoscored website, example of data I received ![image](https://github.com/KirillKlem/player-score-web/assets/57907908/646b00c1-a48b-43ea-b636-ce76633f042b)
* Next, I need to create models for position. To do this, I created a universal pattern, which I used to create all positions, and the signs were inherited using polymorphism, also for each position a separate table was created, inherited from the main one with all the players. Migrations were also used for version control. This is what the example of the main table and their system looked like: ![image](https://github.com/KirillKlem/player-score-web/assets/57907908/5d6a52b4-3c0a-4857-8cba-ea3a95128a9b) ![image](https://github.com/KirillKlem/player-score-web/assets/57907908/cd27675c-e91e-4a40-81f6-6dcb3ca6f791)

