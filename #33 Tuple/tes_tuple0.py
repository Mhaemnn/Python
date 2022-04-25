# List
Ganjil = [1, 3, 5, 7, 9]

# Tuple
Genap = (2, 4, 6, 6, 8, 10)

print(type(Ganjil))
print(type(Genap))

print(Genap)

# Sequence Unpacking (untuk mengekstrak isi dari tuple ke dalam varible tunggal" secara berurutan)

mahasiswa = ('muhaemin', 'bandung', 24)
nama,asal,umur = mahasiswa
print('Nama: ',nama)
print('Asal: ',asal)
print('Umur: ',umur)

# Fungsi bawaan tuple
number = (23,89,100,11,3,4,5,60,77)
max(number) # nilai terbesar
min(number) # nilai terkecil
len(number) # menghitung jumlah item pada tuple
