# belajar StaticMethod & ClassMethod
print(20 * "=" + "StaticMethod & ClassMethod" + 20 * "=")


class Hero:

    # class variable private
    __jumlah = 0

    def __init__(self, name) -> None:
        self.__name = name

        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk object tapi berlaku untuk class
    def getJumalah1():
        return Hero.__jumlah

    # method static (decorator) akan nempel ke object dan classnya
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


nanang = Hero("nanang")
print(Hero.getJumlah2())
rikimaru = Hero("rikimaru")
print(rikimaru.getJumlah2())
ompong = Hero("ompong")
print(Hero.getJumlah3())
