# operator dalam bentuk method
print("\n", 40 * "=", "\n")
# merubah dari case ke string

# merubah semua ke upper case
salam = "hallo!"
print("normal: " + salam)
salam = salam.upper()
print("upper : " + salam)

print("\n", 40 * "-", "\n")

# merubah semua ke lower case
sapa = "JaaaNCokkkkKK"
print("normal: " + sapa)
sapa = sapa.lower()
print("lower : " + sapa)

print("\n", 40 * "-", "\n")

# pengecekan dengan isX method
# contoh pengecekan dengan lower case
senyum = "ketawa"
harus_senyum = senyum.isupper()  # hasilnya boolean
print(senyum + "is upper: " + str(harus_senyum))
harus_senyum = senyum.islower()  # hasilnya boolean
print(senyum + "is lower: " + str(harus_senyum))

print("\n", 40 * "-", "\n")

# isalpha   () <--- untuk mengecek semua huruf
# isalnum   () <--- huruf dan angka
# isdecimal () <--- angka saja
# isspace   () <--- spasi, tub, newline, \n
# istitle   () <--- semua akan dimulai dengan huruf besar
judul = "Remaja Yang kuat"
cek_judul = judul.istitle()
print(judul + "is title: " + str(cek_judul))

print("\n", 40 * "-", "\n")

# mengecek komponen starswith() endswith()
cek_start = "Berharap Banyak".startswith("Berharap")
print("start: " + str(cek_start))

cek_end = "Berharap Banyak".endswith("Banyak")
print("end  : " + str(cek_end))

print("\n", 40 * "-", "\n")

# penggabungan komponen join() spit()
pisah = ['aku', 'sayang', 'kamu']
# bisa menggunakan koma(,) atau spasi(  ) dan atau karekter lain(contoh:ehh)
gabungan = ' ehm '.join(pisah)
print(pisah)
print(gabungan)

# ini akan mencetak string kembali kesemula
gabungan = "aku ehm sayang ehm kamu"
print(gabungan.split("ehm"))


print("\n", 40 * "-", "\n")

# alokasi karakter rjust() ljust() dan center
kanan = "kanan".rjust(10, "-")
print("'" + kanan + "'")

kiri = "kiri".ljust(10, "-")
print("'" + kiri + "'")

tengah = "tengah".center(20, "-")
print("'" + tengah + "'")

# kebalikanya --> strip()
tengah = tengah.strip("-")  # strip untuk menghilangkan tanda -
print("'" + tengah + "'")

print("\n", 40 * "=", "\n")
