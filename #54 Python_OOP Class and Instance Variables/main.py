# Class and Instances Variables
print(10 * "=" + "class and instances variables" + 10 * "=")


class hero:  # template
    # class varibel
    jumlah = 0

    def __init__(self, inputNama, inputHealth, inputPower, inputArmor) -> None:
        # instances varibles
        self.nama = inputNama
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        hero.jumlah += 1
        print("membuat hero dengan nama", inputNama)


hero1 = hero("muhaemin", 100, 1000, 1000000)  # object
print(hero.jumlah)
hero2 = hero("rama", 10, 100, 19)
print(hero.jumlah)
hero3 = hero("asuuuuu", 10000, 1000, 1000)
print(hero.jumlah)


# penjelasan:
"""
1. varible-varible yand diatas seperti: nama, health dll. akan dimiliki oleh si hero1,2,3
2. di dijalankan print(hero.__dict__, maka attribut dari hero tersebut tidak ada)
3. maka harus membuat class varibale, class varible adalah variabel yang ada didalam class itu sendiri
4. 
"""
