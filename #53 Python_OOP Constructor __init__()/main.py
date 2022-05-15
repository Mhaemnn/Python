from traceback import print_tb


print(20 * "=" + "Constructor __init__()" + 20 * "="+"\n")


class Hero:

    def __init__(self, inputName, inputHealth, inputArmor) -> None:
        self.name   = inputName
        self.health = inputHealth
        self.armor  = inputArmor


hero1 = Hero("Hendra", 1000, 100)
hero2 = Hero("Sutisna", 100, 0)
hero3 = Hero("Samdan", 1000, 1000)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__,"\n")



print(62*"=")