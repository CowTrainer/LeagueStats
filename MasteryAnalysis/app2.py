import cassiopeia as cass
from cassiopeia import Summoner
import seaborn as sns
import xlsxwriter
import os

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(os.path.join(os.path.dirname(os.path.abspath(__file__)),"highestpercentage.xlsx"))
worksheet = workbook.add_worksheet()

# Variables
players = []
championsmaster = {}
totalpoints = 0
row = 0
col = 0

        
class champmast:
    """
    A class to represent a champion and it's player dervied stats.

    ...

    Attributes
    ----------
    points : int
        total number of mastery points earned by all players on champion
    top3 : tuple list
        list containing top 3 masters of that champion
    played : int
        number of players that have played that champion

    Methods
    -------
    checkupdate(newpoints, newname):
        Compare new entry to existing top 3 masters and update if necessary
    """
    def __init__(self,points):
        """
        Constructs all the necessary attributes for the champmast object.

        Parameters
        ----------
        points: int
            inital points accumulated on that champion
        """

        self.points = points
        self.top3 = [("default", 0),("default2", 0), ("default3",0)]
        self.played = 0
    def checkupdate(self, newpoints, newname):
        """
        Checks the top 3 masters against a new summoner entry and updates if necessary


        Parameters
        ----------
        newpoints: int
            points of the new summoner entry
        newname: string
            name of the new summoner entry
        
        Returns
        -------
        None
        """
        if (newpoints > self.top3[0][1]):
            self.top3.pop()
            self.top3.insert(0,(newname, newpoints))
        elif (newpoints > self.top3[1][1]):
            self.top3.pop()
            self.top3.insert(1,(newname, newpoints))
        elif (newpoints > self.top3[2][1]):
            self.top3.pop()
            self.top3.insert(2,(newname, newpoints))        

with open('players2.txt') as my_file:
    for line in my_file:
        players.append(line)
        
cass.set_riot_api_key("YOUR_API_KEY")  # This overrides the value set in your configuration/settings.
regionValue = "NA" # Switch to your own region e.g NA, EUW, KR

# Loop through players, get their mastery, and preform needed operations
for x in players:
    summoner = Summoner(name = x.rstrip("\n"), region = regionValue)
    championmastlist = cass.get_champion_masteries(summoner=summoner, region=regionValue)
    for y in championmastlist:
        # Add points if champion entry already exists in mastery list
        if (y.champion.name in championsmaster):
            championsmaster[y.champion.name].points += y.points
        # Else create new champmast object
        else:
            championsmaster[y.champion.name] = champmast(y.points)
        if(y.points > 0):
            championsmaster[y.champion.name].played += 1
        # Add points to total champion mastery points
        totalpoints += y.points
        championsmaster[y.champion.name].checkupdate(y.points, summoner.name)


# Sort champion mastery dictionary by least to most mastered
sortedict = dict(sorted(championsmaster.items(), key=lambda item: item[1].points))
my_file = open("analysis.txt", 'w')

# Write column titles for spreadsheet
worksheet.write(row, col, "Champion")
worksheet.write(row, col + 1, "Biggest player")
worksheet.write(row, col + 2, "Percentage of champion's total mastery they own")
row += 2

for key, value in sortedict.items():
    # Print analysis to analysis.txt
    print("Champion name: " + key, file = my_file)
    print("Total mastery: " + str(value.points), file = my_file)
    print("Mastery percentage: " + "{:.2%}".format(value.points / totalpoints), file = my_file)
    print("Unique players: " + str(value.played), file = my_file)
    print("Top 3 players", file = my_file)
    print("1: " + str(value.top3[0][0]) + " Points: " + str(value.top3[0][1]), file = my_file)
    print("2: " + str(value.top3[1][0]) + " Points: " + str(value.top3[1][1]), file = my_file)
    print("3: " + str(value.top3[2][0]) + " Points: " + str(value.top3[2][1]), file = my_file)
    print("", file = my_file)

    # Write highest percentage of mastery to worksheet
    worksheet.write(row, col, key)
    worksheet.write(row, col + 1, value.top3[0][0])
    worksheet.write(row, col + 2, "{:.2%}".format(value.top3[0][1] / value.points))
    row += 1
workbook.close()