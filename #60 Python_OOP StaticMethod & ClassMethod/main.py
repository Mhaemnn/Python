
# belajar StaticMethod & ClassMethod

print(20 * "=" + "StaticMethod & ClassMethod" + 20 * "="+"\n")


class Hero:
    #private class varible
    __jumlah = 0

    def __init__(self, name):
        self.name = name
        Hero.__jumlah += 1

    #method ini berlaku untuk objek
    def getJumlah1(self):
        return Hero.__jumlah

    #method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah2():
        return Hero.__jumlah

    #method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah3():
        return Hero.__jumlah


    @staticmethod
    def getJumlah4(cls):
        return cls.__Jumlah

adam = Hero("Adam")
print(Hero.getJumlah3())
panji = Hero("Panji")
print(Hero.getJumlah3())
sadaku = Hero("Sadaku")
print(Hero.getJumlah4())
