print(20*"="+"ZeroDivisionError"+20*"=")
print(60*"=")

while True:
  try:
    penyebut  = int(input("Masukan angka penyebuat\t\t: "))
    pembilang = int(input("Masukan angka pembilang\t\t: "))
    hasil     = penyebut / pembilang
    break
  except ZeroDivisionError: # menggunakan zeroDevisionError
    print("Harap masukan angka selain 0")
print("Berhasil, hasil dari pembagian adalah: ",hasil)