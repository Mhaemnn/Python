class Hero:
    # class varibel
    jumlah = 0
    __privateJumlah = 0
    
    def __init__(self, name, health):
        self.name = name
        self.health = health 


        #varible instance private
        self.__private = "private"

        #varible instance protected
        self.__protected = "protected"


Jhon = Hero("Jhon",100)

print(Jhon.__dict__)
print(Hero.__dict__)


"""
1. jika menambahkan sotgan.private = "testing" = akan menghasilkan variable baru
2. sebenernya sotgan.private = "testing" ini adalah assigments sivariable nya keluar dari class
3. 
"""
