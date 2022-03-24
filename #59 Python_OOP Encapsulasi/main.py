# belajar Encapsulasi

class Hero:

    def __init__(self, name, health, attackPower) -> None:
        self.__name = name
        self.__health = health
        self.__attack = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower


# awal dari game
ucup = Hero("ucup", 100, 100)


# game berjalan
# ucup.__name = "rama" ini ga boleh dan gak bisa soalnya akan menghasilkan variable baru
# print(ucup.__name) # ini tidak akan bisa tidak akan mau
print(ucup.getName())
print("awalnya adalah : ", ucup.getHealth())
ucup.diserang(5)
print("sisanya adalah : ", ucup.getHealth())
