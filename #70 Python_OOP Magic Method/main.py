# belajar magic method

class Mahasiswa:

    # magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self) -> str:
        return "Mahasiswa: {} | dengan jumlah: {}".format(self.nama, self.jumlah)

    def __str__(self) -> str:
        return "Mahasiswa: {} | dengan jumlah: {}".format(self.nama, self.jumlah)

    def __add__(self, object):
        return self.jumlah + object.jumlah


pelajar1 = Mahasiswa("nanang", 3)
pelajar2 = Mahasiswa("sudurot", 4)

print(pelajar1)
print(pelajar2)
print(pelajar1 + pelajar2)

# salah satu magic method:
# __init__
# __repr__ biasanya ini dipake saat debuging
# __str__ hampir sama dengan __repr__ biasanya dipake kalau programnya udah siap produksi
# __add__ untuk mengjumlahkan 2 buah object
