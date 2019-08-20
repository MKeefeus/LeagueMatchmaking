class Summoner:

    def __init__(self, name, tier, rank, lp, level):
        self.name = name
        self.tier = tier
        self.rank = rank
        self.lp = int(lp)
        self.level = int(level)
        self.rank_dict = {
            "UNRANKED": 0,
            "IRON": 0,
            "BRONZE": 400,
            "SILVER": 800,
            "GOLD": 1200,
            "PLATINUM": 1600,
            "DIAMOND": 2000,
            "MASTER": 2400,
            "GRANDMASTER": 2800,
            "CHALLENGER": 3200,
            "IV": 0,
            "III": 100,
            "II": 200,
            "I": 300
        }
        self.mmr = self.calculate_mmr()

    def print_data(self):
        print("Name: " + self.name)
        if self.tier and self.rank:
            print("Rank: {} {} {}LP".format(self.tier, self.rank, self.lp))
        elif self.tier:
            print("Rank: {}".format(self.tier))
        print("Level: {}".format(self.level))
        print("MMR: {}\n".format(self.mmr))

    def calculate_mmr(self):
        if self.tier and self.rank and self.lp:

            if self.tier == "CHALLENGER" or "GRANDMASTER" or "MASTER":
                return self.rank_dict[self.tier] + self.lp + self.level

            return self.rank_dict[self.tier] + self.rank_dict[self.rank] + self.lp + self.level

        elif self.tier:
            return self.rank_dict[self.tier] + self.level

        else:
            return self.level
