print(10 * "=" + "Membuat Game Sederhana" + 10 * "="+"\n"+"\n")

class Hero:

    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, Hero):
        print(self.name + ' menyerang ' + Hero.name)
        Hero.diserang(self, self.attackPower)

    def diserang(self, Hero, attackPower_Hero):
        print(self.name + ' diserang ' + Hero.name)
        attack_diterima = attackPower_Hero/self.armorNumber
        print('serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))


nanang = Hero('nanang', 100, 10, 5)
nartoo = Hero('nartoo', 100, 20, 10)

nanang.serang(nartoo)
print("\n")
nartoo.serang(nanang)
