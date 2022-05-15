print(20*"="+"ValueError"+20*"=")
print(50*"=")

while True:
  try:
    penyebut  = int(input("Masukan angka penyebut\t\t: "))
    pembilang = int(input("Masukan angka pembilang\t\t: "))
    hasil     = penyebut / pembilang
    break

  except ValueError: # menambhakan ValueError di sini
    print("Harap masukan angka!!")
print("Berhasil, hasil dari pembagian adalah: ", hasil)