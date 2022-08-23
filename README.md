# LeagueStats
 A flask website that contains multiple programs to analyze League of Legends statistics.
 
 Built with cassiopeia, flask and Chart.js. Live website: https://leaguestats.cf
 
 A description of each application is listed below.
 
## ChampionScale
 A program that creates a Chart.js scatter plot representing mastery on a champion vs total level.
 Use this to find who is the most intense *insert champion here* gamer out of all your friends!
 
## ClashScale
 A program that creates a Chart.js scatter plot representing clash games won
 versus clash games played. Use this to find which one of your friends is the best clash player!
 
## MasteryAnalysis
 A program that analyzes masteries and attempts to find out what the most played champion by your friends is (among other things)!
 
 Will produce two files **analysis.txt** and **highestmastery.xlsx**
 
 **analysis.txt** will have a set of data for each champion, like pictured below.
  ```
  Champion name: Yasuo
  Total mastery: 951100
  Mastery percentage (of all): 5.38%
  Unique players: 10
  Top 3 players
  1: RandomPerson3 Points: 302077
  2: WowSoCoolUser Points: 238116
  3: Shadowlyavenger Points: 149096
  ```
  Total mastery indicates the sum of mastery points accumulated on this champion by all players, 
  Mastery percentage indicates the total percentage of all mastery accumulated on all champions that 
  the champion indicated contributes. Everything else is fairly self explanatory.
  
**highestmastery.xlsx** will have three columns, Champion, biggest player (of that champion), and percentage of mastery they own. You can sort this by the percentage of  mastery owned to find out who the biggest one-tricks are and what champion they one trick!

## Installation
 To ensure you have all required libraries to run these programs, run (while in the LeagueStats directory):
 ```
 pip install -r requirements.txt
 ```
 To ensure that flask knows that we want to run application.py you run:
 ```
 (Windows)
 set FLASK_APP=application
 (Linux/Mac)
 export FLASK_APP=application
 ```
 For your application's secret key, you can either choose to user the default one provided, or (recommended) set your own with:
 ```
 (Windows)
 set SECRET_KEY=secretvalue
 (Linux/Mac)
 export SECRET_KEY=secretvalue
 ```
 Finally, once you have done the above, you can run (in the LeagueStats directory)
 ```
 flask run
 ```
 
 
 
