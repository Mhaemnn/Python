# belajar getter & setter
print(20 * "=" + "Getter & Setter" + 20 * "=")


class Hero:

    def __init__(self, name, health, armorr) -> None:
        self.name = name
        self.health = health
        self.armorr = armorr
        #self.info = "name {} : \n\thealth {}". format(self.name, self.health)

    def getHealth(self):
        return self.__health

    @property
    def info(self):
        return "name {} : \n\thealth {}". format(self.name, self.health)

    @property
    def armorr(self):
        pass

    @armorr.getter
    def armorr(self):
        return self.__armorr

    @armorr.setter
    def armorr(self, input):
        self.__armorr = input

    @armorr.deleter
    def armorr(self):
        print("armorr di delet")
        self.__armorr = None


nanang = Hero("nanang", 100, 10)

print("merubah info")
print(nanang.info)
nanang.name = "mumu"

print("getter dan setter untuk __armorr: ")
print(nanang.armorr)
nanang.__armorr = 50
print(nanang.armorr)

print("delet armorr")
del nanang.armorr
print(nanang.__dict__)
