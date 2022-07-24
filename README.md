# LeagueStats
 A store for all my programs related to League of Legends and statistics
 
 To ensure you have all required libraries to run these programs, run:
 ```
 pip install -r requirements.txt
 ```
 
## ChampionScale
 A program that creates a matplotlib scatter plot representing games played on a champion
 versus the level of that summoner. Can be customized through editing values in the program.
 Use this to find who is the most intense *insert champion here* gamer out of all your friends!
 #### Instructions
 1. Insert the wanted champion, your API_KEY and the region of your summoners that you want to analyze in app.py, like this.
    ```
    TARGET_CHAMPION = "Darius" # Put the champion you want to target here!
    ...
    cass.set_riot_api_key("YOUR_API_KEY")  # Put your API Key here
    cass.set_default_region("NA") # Put your Country Code here.
    ```
 2. Edit the playerslist.txt file to include as many accounts as you want, one per line.
    Example:
    ```
    Hide on Bush
    T1 OK GOOD YES
    Taboany
    ```
    Warning: Riot API does limit amount of calls you can make per second or minute so a large list of accounts may take more time.
 3. Go ahead and run the program! The chart may be ugly so feel free to resize or to add your own beautifying code
    (P.S if you have a way to make the final chart prettier please tell me, I am matplotlib noob)
## ClashScale
 A program that creates a matplotlib scatter plot representing clash games won
 versus clash games played. Use this to find which one of your friends is the best clash player!
 #### Instructions
 1. Insert your API_KEY and the region of your summoners that you want to analyze in clashapp.py, like this.
    ```
    cass.set_riot_api_key("YOUR_API_KEY")  # Put your API Key here
    regionValue = "NA" # Switch to your own region e.g NA, EUW, KR
    ```
 2. Edit the clashlist.txt file to include as many accounts as you want, one per line.
    Example:
    ```
    Hide on Bush
    T1 OK GOOD YES
    Taboany
    ```
    Warning: Riot API does limit amount of calls you can make per second or minute so a large list of accounts may take more time.
 3. Go ahead and run the program! Small note that riot does delete older games in your match history to make room for newer ones,
    so a less frequent gamer might have clash games stored up to a year ago, while a more frequent gamer might only have clash games from 5-6
    months ago. This can affect the amount of clash games that the chart displays.
## MasteryAnalysis
 A program that analyzes masteries and attempts to find out what the most played champion by your friends is (among other things)!
 #### Instructions
 1. Insert your API_KEY and the region of your summoners that you want to analyze in app2.py, like this.
    ```
    cass.set_riot_api_key("YOUR_API_KEY")  # Put your API Key here
    regionValue = "NA" # Switch to your own region e.g NA, EUW, KR
    ```
 2. Edit the players2.txt file to include as many accounts as you want, one per line.
    Example:
    ```
    Hide on Bush
    T1 OK GOOD YES
    Taboany
    ```
 3. Go ahead and run the program! Two files will be modified with the resulting data, analysis.txt and highestmastery.xlsx
 4. analysis.txt will have a set of data for each champion, like pictured below.
    ```
    Champion name: Yasuo
    Total mastery: 951100
    Mastery percentage: 5.38%
    Unique players: 10
    Top 3 players
    1: RandomPerson3 Points: 302077
    2: WowSoCoolUser Points: 238116
    3: Shadowlyavenger Points: 149096
    ```
    Total mastery indicates the sum of mastery points accumulated on this champion by all players, 
    Mastery percentage indicates the total percentage of all mastery accumulated on all champions that 
    the champion indicated contributes. Everything else is fairly self explanatory.
 5. highestmastery.xlsx will have three columns, Champion, biggest player (of that champion), and percentage of mastery they own. You can sort this by the percentage       of mastery owned to find out who the biggest one-tricks are and what champion they one trick!
 
 
