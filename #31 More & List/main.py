# More and list

print(20*"="+"More and list"+20*"="+"\n")

hewan = ['singa','gajah','harimau','kuda','monyet']
print(hewan)

#unutk menambahkan 
hewan.append("sapi")
print(hewan)

# Menggabungkan 2 varible
nama = ['muldoko','sanuri','sokep','rail']
hewan.extend(nama)
print(hewan)

# Menyisipkan data baru di dalam list
hewan.insert(1,90000000)
print(hewan)

# Menghapus elemen dari dalem list menggunakan .remove
hewan.remove("kuda")
print(hewan)

# Menghapus elemen dari dalam list menggunakan .pop
hewan.pop(0)
print(hewan)

# Menghapus keseluruhan elemet list
hewan.clear()
print(hewan)

# Mengurutkan nilai dari yang terkecil ke terbesar
number = [3,90,23,98,100,2,1,5,6,222,88]
number.sort()
print(number)

# Menghitung jumlah karakter 
nama.count("muldoko")

# selain menghitung kata .count bisa untuk menghitung karakter
nama.count("a")

