from asyncio import queues
import cassiopeia as cass
import roleml
from datetime import timedelta
import json

def getAPI_key():
    f = open("api_key.txt", "r")
    return f.read()

cass.set_riot_api_key(getAPI_key())

def get_champ_played(Summoner):

    roles= []
    champID= []
    playedChampion = []

    SummonerName = cass.get_summoner(name = Summoner, region = "NA")
    # print(SummonerName)
    i = 0
    while i < 5:
        match_history = SummonerName.match_history[i]
        champion = match_history.participants[Summoner].champion.id
        champ= champList[str(champion)]
        champID.append(champion)
        playedChampion.append(champ)
        i = i + 1
    
    #print("Champs: ", champ)
    return champ


def get_team(Summoner):

    team = []
    i = 0
    SummonerName = cass.get_summoner(name = Summoner, region = "NA")
    match_history = SummonerName.match_history[i]
    # team.append(match_history.blue_team)
    # print(team)
    print(match_history.TeamData)
  


with open('championFull.json', 'r', encoding="utf8") as champList_file:
    champList = json.load(champList_file)
    champList= champList['keys']
    champList_file.close()
#print(champList)

SummonerName = "Snippzzz"
get_champ_played(SummonerName)
#get_team(SummonerName)
