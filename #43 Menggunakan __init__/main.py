print(40*"=")

class mahasiswa():
    def __init__(self, masukan_nama) -> None:
        self.nama = masukan_nama

    def nilai(self,nilai): # dijalankan ketika di panggil
        if nilai >= 70:
            print(self.nama, 'lulus dengan nilai:',nilai)
        else:
            print(self.nama, 'lulus dengan nilai:', nilai)

muhaemin = mahasiswa("muhaemin iskandar")
print(muhaemin.nama) # dipanggil tampa menggunakan method
muhaemin.nilai(80) # dipanggil dengan menggunakan method
