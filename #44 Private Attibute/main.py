# class
class mahasiswa():

    jurusan = "teknik tata boga"
    __nilai = 0  # private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim  # public

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, 'tidak lulus')
        else:
            print(self.nama, 'lulus')

# main programnya


rahel = mahasiswa("rahel mulyo", 13317001)
samud = mahasiswa("michael samud", 13317002)

rahel.uts(10)
rahel.uas(50)
rahel.check_status()
samud.uts(5)
samud.uas(25)
samud.__nilai = 60
samud.check_status()
