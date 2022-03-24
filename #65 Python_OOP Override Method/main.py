# Belajar override Method

class Hero:
    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health: {}". format(
            self.name,
            self.health
        ))


class Hero_intelligent(Hero):
    def __init__(self, name) -> None:
        super().__init__(name, 100)

    # override
    def showInfo(self):
        print("showInfo di subclass Hero")
        print("{} \n\tType: Intelligent, \n\thealth: {}". format(
            self.name, self.health))


class Hero_strength(Hero):
    def __init__(self, name) -> None:
        super().__init__(name, 200)


mamud = Hero_intelligent("mamud")
dasar = Hero_strength("dasar")

dasar.showInfo()


"""
1. mencoba merubah tipe nya sesuai dengan type nya contoh kalau semisalnya intell ya harus intell lagi.
2. caranya:
    - showInfo di override di clas Hero_intelligent
    - tapi tidak di Hero_strength 
    - dia akan mengoverride sesuatu yang sama 

"""
