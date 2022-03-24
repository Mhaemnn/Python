class hero:  # template
    pass


print(20 * "=" + "pendahuluan: class" + 20 * "=")

hero1 = hero()  # object / instance
hero2 = hero()
hero3 = hero()


hero1.nama = "muhaemin"
hero1.health = 100

hero2.nama = "rama"
hero2.health = 100

hero3.nama = "dani"
hero3.health = 100

print(hero1)
print(hero1.__dict__)
print(hero1.nama)
