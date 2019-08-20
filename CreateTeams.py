from itertools import combinations
from Team import Team


def calc_average_mmr(summoner_list):
    total = 0
    for i in summoner_list:
        total = total + i.mmr
    return total/len(summoner_list)


def check_overlap_players(team1, team2):
    for player1 in team1.player_list:
        for player2 in team2.player_list:
            if player1 == player2:
                return True
    return False


def main(summoner_list):
    average_mmr = calc_average_mmr(summoner_list)
    possible_teams = list(combinations(summoner_list, 5))
    team_list = []
    for i in possible_teams:
        team_list.append(Team(i[0], i[1], i[2], i[3], i[4]))
    best_delta = 1000000  # set to an impossible number to set up first team
    team1 = None
    for team in team_list:
        if abs(team.mmr - average_mmr) < best_delta:
            team1 = team
            best_delta = abs(team.mmr-average_mmr)
    team_list.remove(team1)

    best_delta = 1000000  # do again to find next best team
    team2 = None
    for curr_team in team_list:
        if abs(curr_team.mmr - average_mmr) < best_delta:
            if check_overlap_players(curr_team, team1):
                continue
            else:
                team2 = curr_team
                best_delta = abs(curr_team.mmr - average_mmr)

    teams = team1, team2
    return teams
