import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Getting the API
download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")

#Reading broad details of the dataset
nba = pd.read_csv("nba_all_elo.csv")
'''print(type(nba))
print(len(nba))
print(nba.shape)
print(nba.info())
print(nba.describe(include=object))
print(nba["team_id"].value_counts())
print(nba["fran_id"].value_counts())'''

#manipulating & finding specific data
nba["date_played"] = pd.to_datetime(nba["date_game"])
print(nba.loc[nba["team_id"] == "BOS", "pts"].sum())

print(nba.loc[5555:5559, ["fran_id", "opp_fran", "pts", "opp_pts"]])

find = nba[
    (nba["team_id"].str.startswith("LA")) &
    (nba['year_id'] == 1992) &
    (nba['game_location'] == 'H') &
    (nba["_iscopy"] == 0) &
    (nba['notes'].notna())
]
print(find)

print(nba.groupby("fran_id", sort=True)["pts"].sum())

gameResults = nba[
    (nba["fran_id"] == "Warriors") &
    (nba["year_id"] == 2015)
].groupby(["is_playoffs", "game_result"])["game_id"].count()
print(gameResults)

#small practice dataframe
'''city_revenues = pd.Series(
    [4200, 8000, 6500],
    index=["Amsterdam", "Toronto", "Tokyo"]
)
city_employee_count = pd.Series({"Amsterdam": 5, "Tokyo": 8})
city_data = pd.DataFrame({
    "revenue": city_revenues,
    "employee_count": city_employee_count
})
print(city_data)
print(city_data.index)
print(city_data.values)
print(city_data.axes)

further_city_data = pd.DataFrame(
    {"revenue": [7000, 3400], "employee_count":[2, 2]},
    index=["New York", "Barcelona"]
)
all_city_data = pd.concat([city_data, further_city_data], sort=False)
print(all_city_data)

city_countries = pd.DataFrame({
    "country": ["Holland", "Japan", "Holland", "Canada", "Spain"],
    "capital": [1, 1, 0, 0, 0]},
    index=["Amsterdam", "Tokyo", "Rotterdam", "Toronto", "Barcelona"]
)
cities = pd.concat([all_city_data, city_countries], axis=1, sort=False)
print(cities)'''

#plot 1
knickPntArray = (nba[nba["fran_id"] == "Knicks"].groupby("year_id")['pts'].sum())
plt.subplot(2, 2, 1)
plt.plot(knickPntArray)

plt.title("Knick's Point Total per Season")
plt.xlabel("Years")
plt.ylabel("Season Point Total")

#plot 2
heatWLRatio = (nba[
    (nba["fran_id"] == "Heat") &
    (nba['year_id'] == 2013)
]["game_result"].value_counts())
labels = ["W", "L"]

plt.subplot(2, 2, 4)
plt.pie(heatWLRatio, labels = labels)

plt.title("Heat's Win/Loss Ratio in 2013")
#plt.legend(title = "Win/Loss Ratio:", loc = 'lower left')

plt.suptitle("NBA DATA")
plt.show()

#cleaning up data
df = nba.copy()
df["date_game"] = pd.to_datetime(df["date_game"])
df["game_location"] = pd.Categorical(df["game_location"])
df["game_location"].dtype
df["game_result"] = pd.Categorical(df["game_result"])
print(df["game_result"].value_counts())
df.info()

print(nba.describe())