class Hero:
    # class variable
    jumlah_hero = 0
    __privateJumlah = 0

    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health

        # variable instances private
        self.__private = "ini adalah private"

        # varible instances protected
        self._protected = "protected"


sotgan = Hero("sotgan", 100)

# print(sotgan.__dict__) #untuk melihat dictionary apa yang di miliki

print(sotgan.__dict__)
sotgan.__private = "testing"
print(sotgan.__dict__)


"""
1. jika menambahkan sotgan.private = "testing" = akan menghasilkan variable baru
2. sebenernya sotgan.private = "testing" ini adalah assigments sivariable nya keluar dari class
3. 
"""
