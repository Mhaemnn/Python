# belajar method
from unicodedata import name


print(20 * "=" + "OOP-Method" + 20 * "="+'\n')


class Hero:

    # class variable
    jumlah = 0

    def __init__(self, inputName, inputHeatlh, inputPower, inputArmor) -> None:
        # instance varible
        self.name = inputName
        self.health = inputHeatlh
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    # Membuat method
    # method tampa return tampa argumen
    def who(self):
        print("my name is: ",self.name)

    # method dengan argument tampa return
    def healthUp(self,up):
        self.health  += up


hero1 = Hero("Hendra", 100, 100, 100)    
hero2 = Hero("Sanawi", 100, 10, 0)

hero1.who()
hero1.healthUp(20)





print(50*"=")