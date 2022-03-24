class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)


class Tipe_Hero:
    def setTipe(self, tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)


class Hero(Team, Tipe_Hero):
    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health


nanang = Hero("nanang", 100)

nanang.setTeam("red")
nanang.setTipe("berani")

nanang.showTeam()
nanang.showTipe()
