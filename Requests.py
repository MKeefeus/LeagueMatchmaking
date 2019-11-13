import requests
import json
summonerName = 'JuicyJush'
key = 'RGAPI-850c80e7-ae57-4bee-ace7-8653d706b838'
r = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{0}?api_key={1}'
                 .format(summonerName, key))
JSON = r.json()["id"]
summonerID = JSON["id"]
leagueInfo = requests.get('https://na1.api.riotgames.com//lol/league/v4/entries/by-summoner/{0}?api_key={1}'
                          .format(summonerID, key))
print(json.dumps(leagueInfo.json(), indent=4))

