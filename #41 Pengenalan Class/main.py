class Mahasiswa():
    nama = 'nama'
    umur = 24
    status = 'mahasiswa'
    jk = 'laki'


mahasiswa_1= Mahasiswa()
mahasiswa_1.nama = 'Fahreza'
mahasiswa_1.umur = 24
mahasiswa_1.status = 'single'
mahasiswa_1.jk = 'laki-laki'

mahasiswa_2 = Mahasiswa()
mahasiswa_2.nama = 'Maemunah'
mahasiswa_2.umur = 50
mahasiswa_2.status = 'janda'
mahasiswa_2.jk = 'perempuan'

print('mahasiswa 1',mahasiswa_1.nama, mahasiswa_1.umur, mahasiswa_1.status, mahasiswa_1.jk)
print('mahasiswa 2',mahasiswa_2.nama, mahasiswa_2.umur, mahasiswa_2.status, mahasiswa_2.jk)
