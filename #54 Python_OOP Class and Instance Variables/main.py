# Class and Instances Variables
print(10 * "=" + "class and instances variables" + 10 * "="+"\n")

class Hero: # class / template
    jumlah = 0 # class varible / static varible 

    def __init__(self, inputNama, inputHealth, inputArmor) -> None:
        # instance varible
        self.nama   = inputNama
        self.health = inputHealth
        self.armor  = inputArmor
        Hero.jumlah += 1
        print("NAME HERO",inputNama, "HEALTH",inputHealth, "ARMOR",inputArmor )

hero1 = Hero("HENDREA", 100, 10)
print(Hero.jumlah)
hero2 = Hero("SUTISNA", 100, 100)
print(Hero.jumlah)
hero3 = Hero("SURYANA", 100,100)
print(Hero.jumlah,"\n")





print(49*"=")

# penjelasan:
"""
1. varible-varible yand diatas seperti: nama, health dll. akan dimiliki oleh si hero1,2,3
2. di dijalankan print(hero.__dict__, maka attribut dari hero tersebut tidak ada)
3. maka harus membuat class varibale, class varible adalah variabel yang ada didalam class itu sendiri
4. 
"""
