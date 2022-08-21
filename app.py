from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import cassiopeia as cass
from cassiopeia import Summoner
import xlsxwriter
import os
from io import BytesIO, StringIO
import zipfile


app = Flask(__name__, static_folder="assets")

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                   for root_path, dirs, files in os.walk(folder)
                   for f in files))
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



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/championscale", methods=["GET", "POST"])
def championscale():
    if request.method == "POST":
        API_KEY = request.form.get("API_KEY").strip()
        champion = request.form.get("champion")
        players = request.form.get("playerlist").split('\n')
        region = request.form.get("region")
        mastery, levels, names = ([] for i in range(3))
        cass.set_riot_api_key(API_KEY)
        # Loop through players, extract mastery on champion and player level
        for player in players:
            summoner = Summoner(name = player.strip(), region = region)
            # Test if summoner doesn't exist or API key is invalid
            try:
                if not summoner.exists:
                    flash("One or more summoners are invalid.")
                    return redirect(url_for("championscale"))
            except cass.datastores.common.HTTPError:
                flash("API KEY is invalid.")
                return redirect(url_for("championscale"))
            champMast = cass.get_champion_mastery(
            champion = champion, summoner = summoner,
            region = region,
            )
            mastery.append(champMast.points)
            levels.append(summoner.level)
            names.append(player.strip())
        return render_template("champresults.html", xaxis = levels, yaxis = mastery, zvals = names,
                                last_updated = dir_last_updated("assets/js"), champion = champion.upper())
    else:
        champions = []
        with open('assets/champions.txt') as my_file:
            for line in my_file:
                champions.append(line.rstrip('\n'))
        return render_template("championscale.html", champions = champions)

@app.route("/clashscale", methods=["GET", "POST"])
def clashscale():
    if request.method == "POST":
        ## get form data
        API_KEY = request.form.get("API_KEY").strip()
        players = request.form.get("playerlist").strip().split('\n')
        region = request.form.get("region")
        gamesPlayed, wins, names = ([] for i in range(3))
        cass.set_riot_api_key(API_KEY)
        for player in players:
            summoner = Summoner(name = player.strip(), region = region)
            # Test if summoner doesn't exist or API key is invalid
            try:
                if not summoner.exists:
                    flash("One or more summoners are invalid.")
                    return redirect(url_for("clashscale"))
            except cass.datastores.common.HTTPError:
                flash("API KEY is invalid.")
                return redirect(url_for("clashscale"))
            match_h = cass.get_match_history(
            continent = summoner.region.continent,
            puuid = summoner.puuid, region = region,
            queue = cass.data.Queue("CLASH")
            )
            gamesPlayed.append(len(match_h))
            names.append(player.strip())
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
        return render_template("clashresults.html", xaxis = gamesPlayed, yaxis = wins, zvals = names,
                                last_updated = dir_last_updated("assets/js"))                
    else:
        return render_template("clashscale.html")

@app.route("/masteryanalysis", methods=["GET", "POST"])
def masteryanalysis():
    if request.method == "POST":
        API_KEY = request.form.get("API_KEY").strip()
        players = request.form.get("playerlist").strip().split('\n')
        region = request.form.get("region")
        cass.set_riot_api_key(API_KEY)
        championsmaster = {}
        totalpoints = 0
        # Loop through players, get their mastery, and preform needed operations
        for player in players:
            summoner = Summoner(name = player.strip(), region = region)
            # Test if summoner doesn't exist or API key is invalid
            try: 
                if not summoner.exists:
                    flash("One or more summoners are invalid.")
                    return redirect(url_for("masteryanalysis"))
            except cass.datastores.common.HTTPError:
                flash("API KEY is invalid.")
                return redirect(url_for("masteryanalysis"))
            championmastlist = cass.get_champion_masteries(summoner=summoner, region=region)
            for y in championmastlist:
                # Add points if champion entry already exists in mastery dict
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

        # Create in-memory files and assign them to be written to
        text = StringIO()
        spreadsheet = BytesIO()
        workbook = xlsxwriter.Workbook(spreadsheet, {'in_memory': True})
        worksheet = workbook.add_worksheet()

        # Write headers for file
        row = 0
        col = 0
        worksheet.write(row, col, "Champion")
        worksheet.write(row, col + 1, "Biggest player")
        worksheet.write(row, col + 2, "Percentage of champion's total mastery they own")
        row += 2

        for key, value in sortedict.items():
            # Print analysis to text stream
            text.write("Champion name: " + key + '\n')
            text.write("Total mastery: " + str(value.points) + '\n')
            text.write("Mastery percentage: " + "{:.2%}".format(value.points / totalpoints) + '\n')
            text.write("Unique players: " + str(value.played) + '\n')
            text.write("Top 3 players\n")
            text.write("1: " + str(value.top3[0][0]) + " Points: " + str(value.top3[0][1]) + '\n')
            text.write("2: " + str(value.top3[1][0]) + " Points: " + str(value.top3[1][1]) + '\n')
            text.write("3: " + str(value.top3[2][0]) + " Points: " + str(value.top3[2][1]) + '\n')
            text.write('\n')

            # Write highest percentage of mastery to worksheet
            worksheet.write(row, col, key)
            worksheet.write(row, col + 1, value.top3[0][0])
            if(value.points == 0):
                worksheet.write(row, col + 2, "N/A")
            else:
                worksheet.write(row, col + 2, "{:.2%}".format(value.top3[0][1] / value.points))
            row += 1
        workbook.close()
        mf = BytesIO()
        with zipfile.ZipFile(mf, mode ='w', compression=zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("analysis.txt", text.getvalue())
            zf.writestr("highestmastery.xlsx", spreadsheet.getvalue())
        text.close()
        spreadsheet.close()
        mf.seek(0)
        return send_file(mf, as_attachment=True, attachment_filename='results.zip')
    else:
        return render_template("masteryanalysis.html")

@app.route("/presets")
def presets():
    return render_template("presets.html")
