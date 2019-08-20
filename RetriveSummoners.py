import requests
from Summoner import Summoner
import os


def get_summoner(summoner_name, key):

    summoner_data = (requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{0}?api_key={1}'
                                  .format(summoner_name, key))).json()
    summoner_name = summoner_data['name']    # Updates summoner_name variable to prevent SQL injection
    summoner_id = summoner_data["id"]
    league_info = (requests.get('https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{0}?api_key={1}'
                                .format(summoner_id, key))).json()
    if len(league_info) == 0:
        summoner = no_ranked_data(summoner_data, summoner_name, key)
    elif len(league_info) == 1 and league_info[0]['queueType'] == 'RANKED_SOLO_5x5':
        summoner = ranked_data(summoner_data, summoner_name, league_info)
    elif len(league_info) > 1:
        summoner = multiple_queues_data(summoner_data, summoner_name, league_info, key)
    return summoner


def no_ranked_data(summoner_data, summoner_name, key):
    account_id = summoner_data["accountId"]
    game_reference = (requests.get('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
                                   '{0}?endIndex=1&api_key={1}'.format(account_id, key)).json())
    match_id = game_reference["matches"][0]["gameId"]
    game_data = (requests.get('https://na1.api.riotgames.com/lol/match/v4/matches/{0}?api_key={1}'
                              .format(match_id, key))).json()
    for i in game_data["participantIdentities"]:
        if str(i['player']["summonerName"]).lower() == str(summoner_name).lower():
            participant_id = int(i['participantId']) - 1
    if 'highestAchievedSeasonTier' in game_data['participants'][participant_id]:
        tier = game_data['participants'][participant_id]['highestAchievedSeasonTier']
        summoner = Summoner(summoner_name, tier, None, 0, summoner_data['summonerLevel'])
        return summoner
    else:
        summoner = Summoner(summoner_name, 'UNRANKED', None, 0, summoner_data['summonerLevel'])
        return summoner


def ranked_data(summoner_data, summoner_name, league_info):
    summoner = Summoner(summoner_name, league_info[0]['tier'], league_info[0]['rank'],
                        league_info[0]['leaguePoints'], summoner_data['summonerLevel'])
    return summoner


def multiple_queues_data(summoner_data, summoner_name, league_info, key):
    for i in range(len(league_info)):
        if league_info[i]["queueType"] == "RANKED_SOLO_5x5":
            summoner = Summoner(summoner_name, league_info[i]['tier'], league_info[i]['rank'],
                                league_info[0]['leaguePoints'], summoner_data['summonerLevel'])
            return summoner
    no_ranked_data(summoner_data, summoner_name, key)


def main(usernames):
    key = os.environ['API_KEY']
    print('\n')
    usernames = ['Mkeefeus', 'JuicyJush', 'kmurray12', 'FodgeWaffle', 'Impact', 'Sneaky', 'C9 Sneaky',
                 'Doublelift', 'Xmithie', 'Zaga']
    summoner_list = []
    for i in usernames:
        if i != '':
            summoner_list.append(get_summoner(i, key))
    return summoner_list

