print(10 * "=" + "Membuat Game Sederhana" + 10 * "="+"\n"+"\n")
class Hero:

    def __init__(self,name, health, attackPower, armorPower) -> None:
        self.name   = name
        self.health = health
        self.attack = attackPower
        self.armor  = armorPower

    def serang(self, lawan):
        print(self.name, " menyerang ", lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self,lawan,attackPower_lawan):
        print(self.name, " diserang ", lawan.name)