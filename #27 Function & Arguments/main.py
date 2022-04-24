# Fungsi dengan menggunakan arguments sederhana

print(50*"="+"\n")

def mahasiswa(nama):
    print("siswa ini bernama\t:", nama)

mahasiswa("marzuki")


# Fungsi dengan menggunakan keywords arguments
print(15*"-"+"keywords arguments"+14*"-"+"\n")
def dosen(nama,matul):
    print(f"dosen ini bernama\t: {nama}")
    print(f"matakuliah\t\t: {matul}")

dosen(nama='samud', matul='kalkulus')

# Fungsi dengan menggunkan default arguments
print(15*"-"+"default arguments"+15*"-"+"\n")
def keuangan(nama,shif='siang',kasbon='boleh'):
    print(f"nama keuangan \t\t: {nama}")
    print(f"shif \t\t\t: {shif}")
    print(f"kasbon \t\t\t: {kasbon}")

keuangan('nana')
keuangan("sarif",shif='malam', kasbon='tidak')



print(50*"="+"\n")