print(20*"="+"Inheritance"+20*"=")
class orang:
    def __init__(self,nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f"perkenalkan nama saya {self.nama} dari {self.asal}")

Pujo = orang('pujo','malang')
Pujo.perkenalan()


#membuat class turunan dengan cara mengirimkan class induk sebagai parameter
class pelajar(orang):
    pass

muhaemin = orang("muhaemin", "bandung")
muhaemin.perkenalan()

#membuat constructor pada class turunan
