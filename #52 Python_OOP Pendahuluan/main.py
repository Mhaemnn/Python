from email.base64mime import header_length


class Hero:
    pass

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name   = "Hendra"
hero1.health = 1000

hero2.name   = "Dasep"
hero2.health = 900

hero3.name   = "Suryana"
hero3.health = 3990

print(hero3)
print(hero3.__dict__)
print(hero3.name, hero3.health)