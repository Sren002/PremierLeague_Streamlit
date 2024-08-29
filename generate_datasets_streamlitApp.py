import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/Sren002/web-scraping-PremierLeagueML/main/matches.csv")

teams = df["Team"].unique()
for team in teams:
    # sort data by team name
    data = df.loc[df['Team'] == "%s" % (team)]

    for i in range(2024, 2020, -1):
        # sort database by year
        date = data.loc[(data["Season"].astype(str)) == str(i)]
        
        # sort data by wins, draws, and losses
        wins = date.loc[date["Result"] == "W"]
        draws = date.loc[date["Result"] == "D"]
        losses = date.loc[date["Result"] == "L"]

        # remove whitespace so there are no issues with accessing the file
        team_name = team.replace(" ", "_")
        path = "C:\School\VSCode_Files\generated_data_PremierLeague{}\\".format("_"+str(i))
        csv_name = "{}_{}.csv".format(team_name, i)

        # if the database is not empty, create a csv file in the given path
        if not wins.empty:
            wins.to_csv(path+"Wins_"+csv_name)
        if not draws.empty:
            draws.to_csv(path+"Draws_"+csv_name)
        if not losses.empty:
            losses.to_csv(path+"Losses_"+csv_name)
        
        

        