from tkinter import N


print(10*"="+" Class Variable & Docstring "+10*"="+"\n")
# class
class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim  # public
        mahasiswa.jumlah_mahasiswa += 1

# main programnya


Fahreza = mahasiswa("Fahreza Munawar", 13317001)
Muhamad = mahasiswa("Muhamad Kiki", 13317002)
Dede    = mahasiswa("Dede Ilham", 13317002)

print(mahasiswa.jumlah_mahasiswa)
