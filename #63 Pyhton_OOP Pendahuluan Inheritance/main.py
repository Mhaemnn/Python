# Belajar Iheritances
print(20 * "=" + "Inheritance" + 20 * "=")


class Hero:

    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health


class Hero_intelligent(Hero):
    pass


class Hero_strength(Hero):
    pass


sadad = Hero("sadad", 100)
munaa = Hero_intelligent("munaa", 299)
ext = Hero_strength("ext", 23)

print(sadad.name)
print(munaa.name)
print(ext.name)
