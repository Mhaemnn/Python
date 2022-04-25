# Global scope dan locl scope

# Local scope
data = "sepatu"
def rubahData(dataBaru):
    data = dataBaru #local
    print("data ini di ubah menjadi: ",data)

rubahData('sendal')
print('data\t\t\t: ',data)

print("\n"+60* "="+"\n")


# Global scope
data = "buku fisika"
def rubahData(dataBaru):
    global data # kita telah mengakses variable data di dalam fungsi dengan secara global
    data = dataBaru
    print("data ini di ubah menjadi: ",data)

rubahData('buku kimia')
print('data\t\t\t: ',data)

print("\n"+60* "="+"\n")
# Global scope dengan 2 fungsi
dataSatu = 'isi data satu'
dataDua = 'isi data dua'

def rubahDataSatu(dataBaru):
    global dataSatu
    dataSatu = dataBaru
    print('data ini di ubah menjadi: ',dataSatu)

def rubahDataDua(data,nama):
    global dataSatu, dataDua
    dataSatu = data
    dataDua = nama

rubahDataSatu('data tiga')
rubahDataDua('data lima','data terakhir')

print('data ini di ubah menjadi: ',dataSatu,'dan data',dataDua)

