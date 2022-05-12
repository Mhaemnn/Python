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
            print(self.nama, 'Tidak Lulus')
        else:
            print(self.nama, 'Lulus')

# main programnya


Samsudin = mahasiswa("Samsudin Nugroho: ", 13317001)
Paijo = mahasiswa("Michael Paijo\t: ", 13317002)

Samsudin.uts(10)
Samsudin.uas(50)
Samsudin.check_status()
Paijo.uts(5)
Paijo.uas(25)
Paijo.__nilai = 60
Paijo.check_status()
