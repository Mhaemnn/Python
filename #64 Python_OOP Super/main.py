# Belajar Super

print(20 * "=" + "Super" + 20 * "=")


class Hero:  # super class
    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan helath {}". format(self.name, self.health))


class Hero_intelligent(Hero):  # sub class
    def __init__(self, name) -> None:
        #Hero.__init__(self, name, 100)
        super().__init__(name, 100)
        super().showInfo()  # ini untuk memanggil showInfo


class Hero_strength(Hero):
    def __init__(self, name) -> None:
        #Hero.__init__(self, name, 200)
        super().__init__(name, 200)
        super().showInfo()


mahmud = Hero_intelligent("mahmud")
sumori = Hero_strength("sumori")

print(mahmud.name, " ", mahmud.health)
print(sumori.name, " ", sumori.health)
