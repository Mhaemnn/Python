print(20*"="+"Inheritance"+20*"=")
class orang:
    def __init__(self,nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f"perkenalkan nama saya {self.nama} dari {self.asal}")

Pujo = orang('pujo','malang')
Pujo.perkenalan()

bambang = orang("bambang", "nganjuk")
bambang.perkenalan()

nasir = orang("nasir","bandung")
nasir.perkenalan()