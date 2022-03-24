print(20 * "=" + "Constructor __init__()" + 20 * "=")


class hero:

    def __init__(self, inputNama, inputPower, inputHealth) -> None:
        self.nama = inputNama
        self.power = inputPower
        self.Health = inputHealth


hero1 = hero("muhaemin", 100, 100)
hero2 = hero("rama", 100, 10)
hero3 = hero("dani", 100, 0)


print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
