class Team:

    def __init__(self, player1, player2, player3, player4, player5):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.player5 = player5
        self.mmr = self.calculate_mmr()
        self.player_list = [self.player1, self.player2, self.player3, self.player4, self.player5]

    def calculate_mmr(self):
        total = self.player1.mmr + self.player2.mmr + self.player3.mmr + self.player4.mmr + self.player5.mmr
        return total / 5

    def print_team(self):
        for player in self.player_list:
            player.print_data()
        print('Team MMR: {}\n'.format(self.mmr))
