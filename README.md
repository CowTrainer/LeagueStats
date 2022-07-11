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
 1. Insert the wanted champion, your API_KEY and the region of your summoners that you want to analyze in app.py, like this
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
 1. Insert your API_KEY and the region of your summoners that you want to analyze in clashapp.py, like this
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
    
 
 
 
