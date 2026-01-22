# Write a class Team and define __len__ to return team size and __add__ to merge teams.
class Team:
    def __init__(self,members):
        self.members=members
    def __len__(self):
        return len(self.members)
    def __add__(self,other):
        return Team(self.members+other.members)

team1 = Team(["Alice", "Bob","Kirtan"])
team2 = Team(["Charlie"])

team3 = team1 + team2

print(len(team1))
print(team3.members)

