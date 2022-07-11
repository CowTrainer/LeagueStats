import cassiopeia as cass
from cassiopeia import Summoner
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


players = []
gamesPlayed = []
wins = []
names = []
# Read in players
with open('clashlist.txt') as my_file:
    for line in my_file:
        players.append(line)
        
cass.set_riot_api_key("YOUR-API-HERE")
regionValue = "NA" # Switch to your own region e.g NA, EUW, KR

# For every player, query for match history, and count clash wins + clash games played
for count,x in enumerate(players):
    summoner = Summoner(name = x.rstrip("\n"), region = regionValue)
    match_h = cass.get_match_history(
    continent = summoner.region.continent,
     puuid = summoner.puuid, region = regionValue,
      queue = cass.data.Queue("CLASH")
    )
    gamesPlayed.append(len(match_h))
    names.append(x.rstrip("\n"))
    countWins = 0
    for match in match_h:
        # For some reason teams show up as null unless you "preload" them with a command like queue
        print(match.queue)
        if(match.blue_team.win):
            if summoner in match.blue_team.participants:
                countWins += 1
        else:
            if summoner in match.red_team.participants:
                countWins += 1
    wins.append(countWins)
sns.set(style="dark")
fig, ax = plt.subplots()
ax.scatter(gamesPlayed, wins)
# Plot with line of best fit
plt.plot(np.unique(gamesPlayed), np.poly1d(np.polyfit(gamesPlayed, wins, 1))(np.unique(gamesPlayed)))

for i, txt in enumerate(names):
    ax.annotate(txt, (gamesPlayed[i], wins[i]))
plt.title("The CLASH scale")    
plt.xlabel("Clash games Played")
plt.ylabel("Clash games Won")
plt.show()
