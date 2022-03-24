# belajar method
print(20 * "=" + "OOP-Method" + 20 * "=")


class Hero:
    # class variable

    jumlah_hero = 0

    def __init__(self, inputNama, inputHeatlh, inputPower, inputArmor) -> None:
        # instances
        self.name = inputNama
        self.health = inputHeatlh
        self.power = inputPower
        self.armor = inputArmor

        Hero.jumlah_hero += 1

    # method tampa return & argument, di bahas lain(void function)
    def siapa(self):
        print("namaku adalah " + self.name)

    # method dengan argument tampe return
    def healthUp(self, Up):
        self.health += Up

    # method dengan return
    def Gethealth(self):
        return self.health


hero1 = Hero("muhaemin", 1000, 1001, 1000)
hero2 = Hero("rama", 183, 0, 88)
hero3 = Hero("nanang", 100, 68, 900)
hero4 = Hero("ucup", 299, 89, 0)

hero1.siapa()
hero1.healthUp(290)

print(hero1.Gethealth())
