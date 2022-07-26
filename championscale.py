import cassiopeia as cass
from cassiopeia import Summoner
import matplotlib.pyplot as plt
import seaborn as sns

TARGET_CHAMPION = "Darius" # Put the champion you want to target here!
players = []
games = []
levels = []
names = []
with open('players.txt') as my_file:
    for line in my_file:
        players.append(line)
        
cass.set_riot_api_key("YOUR_API_KEY")  # Put your API Key here
regionValue = "NA" # Switch to your own region e.g NA, EUW, KR

# Loop through players, extract number of games played with champion and player level
for count,x in enumerate(players):
    summoner = Summoner(name = x.rstrip("\n"), region = regionValue)
    match_h = cass.get_match_history(
    continent = summoner.region.continent,
     puuid = summoner.puuid, region = regionValue,
      queue = cass.data.Queue("CLASH")
    )
    games.append(len(match_h))
    levels.append(summoner.level)
    names.append(x.rstrip("\n"))

# Setup scatter plot for data plotting
sns.set(style="dark")
fig, ax = plt.subplots()
ax.scatter(levels, games)

# Plot number of games played on champion and user level on scatter plot
for i, txt in enumerate(names):
    ax.annotate(txt, (levels[i], games[i]))

# Display chart with labels
plt.title("The " + TARGET_CHAMPION + " Scale")    
plt.xlabel("Level")
plt.ylabel("Games played")
plt.show()
