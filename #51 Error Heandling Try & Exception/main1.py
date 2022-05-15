print(20*"="+"Error Try and Execpt"+20*"=")
print(60*"="+"\n")

while True:
  try:
    penyebut  = int(input("Masukan angka penyebut\t\t: "))
    pembilang = int(input("Masukan angkan pembilang\t: "))
    hasil     = penyebut / pembilang
    break
  except:
    print("Harap memasukan angka!!")

print("Berhasil, hasil pembagian adalah: ", hasil)