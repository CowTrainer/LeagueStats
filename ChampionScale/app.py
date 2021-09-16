# NOTICE. This code is deprecated as of Sep 13th 2021 since it uses V4-Match

import cassiopeia as cass
import matplotlib.pyplot as plt
import seaborn as sns

# Initalize target champion, arrays and fill players array
TARGET_CHAMPION = "Darius" # Put the champion you want to target here!
players = []
games = []
levels = []
names = []
with open('playerslist.txt') as my_file:
    for line in my_file:
        players.append(line)
        
cass.set_riot_api_key("YOUR_API_KEY")  # Put your API Key here
cass.set_default_region("NA") # Put your Country Code here.

# Loop through players, extract number of games played with champion and player level
for count,x in enumerate(players):
    person = cass.get_summoner(name = x.rstrip("\n"))
    match_history = cass.get_match_history(summoner=person , champions={cass.get_champion(TARGET_CHAMPION)})
    games.append(len(match_history))
    levels.append(person.level)
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
