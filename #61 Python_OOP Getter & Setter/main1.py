class Karywawan(object):
    def __init__(self, *args, **kwargs):
        self.__nik = kwargs.get('nim', '1111')
        self.__nama = kwargs.get('nama', 'Yanwar Solahudin')
        self.__divisi = kwargs.get('divisi', 'Group of Digital')
        self.__jabatan = kwargs.get('jabatan', 'Backend')
    @property
    def nik(self):
        return self.__nik
    @nik.setter
    def nik(self, nik):
        self.__nik = nik
    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama
    @property
    def divisi(self):
        return self.__divisi
    @divisi.setter
    def divisi(self, divisi):
        self.__divisi = divisi
    @property
    def jabatan(self):
        return self.__jabatan
    @jabatan.setter
    def jabatan(self, jabatan):
        self.__jabatan = jabatan
Karywawan = Karywawan()
Karywawan.nik = "2232"
print(Karywawan.nik)