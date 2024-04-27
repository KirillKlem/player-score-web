## Introduction
Hello! This is an experimental web project (that is, it runs exclusively on the locale).  Its essence is to calculate the rating of football players in the strongest leagues based on their performance. It is worth noting that the project is divided into two micro-services (I am a contributor to both). The second one collected data and sent it using requests [second micro-service](https://github.com/Sashkhalimov/player-score-data-collection/tree/main)

## Requirements
* programming language Python3 and its libraries:
  + Web framework [Flask](https://flask.palletsprojects.com/en/3.0.x/)
  + Library for parsing data from the necessary sites [Soccrdata](https://soccerdata.readthedocs.io/en/latest/intro.html)
* sql toolkit [SQLAlchemy](https://www.sqlalchemy.org)

## Some details that have been paid attention to (i.e. studied in depth)
- Splitting a project into microservices using requests
- Creating high-quality gitignore, requirements.txt , config. Teamwork (2 more people contributed to this project, who are contributors in github repo and partially helped in the implementation of my idea), which has been simplified with the help of the above points.
- The player classes are created using sqlalchemy.orm. Polymorphism was used, including polymorphism for tables that are directly related to player classes
- The architecture of the project. Blueprint and cli are used. The whole project is divided into understandable blocks and meets many development standards.
- Marshmallow was used in conjunction with flask and sqlalchemy, which proved to be an good solution.
- Migrations were used to control the versions of the database, which constantly needs to be updated using requests from the second microservice

## Here's what was implemented
* Firstly, it was necessary to get data about football players, for this I used soccerdata, which provided data from the FBref website, example of data I received ![image](https://github.com/KirillKlem/player-score-web/assets/57907908/b8066471-0bdb-4a5c-924c-6734cbff45fa)
* Next, I need to create models for position. To do this, I created a universal pattern, which I used to create all positions, and the signs were inherited using polymorphism, also for each position a separate table was created, inherited from the main one with all the players. Migrations were also used for version control. This is what the example of the main table and their system looked like: ![image](https://github.com/KirillKlem/player-score-web/assets/57907908/5d6a52b4-3c0a-4857-8cba-ea3a95128a9b) ![image](https://github.com/KirillKlem/player-score-web/assets/57907908/cd27675c-e91e-4a40-81f6-6dcb3ca6f791)
* To calculate the score of the players, I used a weighted average, and the weights themselves were constants set manually (different for each position). Moreover, the main weighted average value for the position was calculated relative to other weighted averages logically grouped.
* The final site looks like this:
![image](https://github.com/KirillKlem/player-score-web/assets/57907908/3becc2b9-c9a0-4da0-9a20-7481e090741a)
+ There are filters for the football team: ![image](https://github.com/KirillKlem/player-score-web/assets/57907908/6d9e5392-4941-4bd5-bd05-81c40cfe8c9c)
+ Statistics for each player: ![image](https://github.com/KirillKlem/player-score-web/assets/57907908/c346a5f7-b334-4bc5-85a6-9e99ecf7dc96)
+ There is also an admin panel ![image](https://github.com/KirillKlem/player-score-web/assets/57907908/beb847e1-1e88-4a04-988b-d85af6c7544e)


