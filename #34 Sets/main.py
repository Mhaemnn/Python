# Belajar set python

# Menggunakan kurung kurawal
mahasiswa = {'sukor','lekyor','manupakturing','donet'}
print(mahasiswa)

# Mengkonversi list ke dalam set
hewan = (['kuda','domba','cicak','kerdil'])
print(hewan)

# set dengan tipe data campuran
campuran = {"kamu","siapa",98489,True,('a','b','c')}
print(campuran)

# Menambahkan element baru
campuran.add('babi')
print(campuran)

# Mengupdate/menambahkan lebih dari satu element
campuran.update({"asu","ajag"})
print(campuran)

print("=======================================================")
"""
# Menghapus anggota
1.remove(nilai) -> menghapus yang di cari, jika tidak ada makan akan error
2.discard(nilai) -> -> menghapus yang di cari, jika tidak ada makan akan error
3.pop() -> mengambil dan menghapus nilai di sebelah kiri
4.clear()
"""
campuran.remove("asu")
print(campuran)
campuran.discard("babi")
print(campuran)
yangDihapus = campuran.pop()
print("element yang dihapus: ",yangDihapus)
print(campuran)
campuran.clear()
#print(campuran)

"""
# Fungsi keanggotaan set
1. union(gabungan)
2.intersection(irisan)
3.difference(selisih)
4.symmetric difference(komplement)
5. dll

"""
print("=======================================================")
#union
SMP = {"mujaka","nobles","rx-4","manulika"}
SMA = {"saroh","kiron","tahu","mujaka"}

#print(SMP | SMA) # bisa menggunakan yang atas atau bawah
print(SMP.union(SMA))

#intersection
print(SMP & SMA)

#difference
print(SMP - SMA)

#
print(SMP.symmetric_difference (SMA))