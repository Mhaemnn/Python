
print("="*35)
print("Operasi Aritmaika")
print("1. Pemjumlah     \t\t [ + ]")
print("2. Pengurang     \t\t [ - ]")
print("3. Perkalian     \t\t [ * ]")
print("4. Pembagian     \t\t [ / ]")
print("5. Modulus       \t\t [ % ]")
print("6. Floor Devision\t\t [ //]")
print("="*35)

operasi = input("Pilih Operasi |1|2|3|4|5|6| \t: ")
bilangan1 = eval(input("Masukan bilangan pertama\t: "))
bilangan2 = eval(input("Masukan bilangan kedua \t\t: "))

#Percabangan
print("="*35)
if operasi == "1":
  print("User memilih penjumlahan")
elif operasi == "2":
  print("User memilih Pengurangan")
elif operasi == "3":
  print("User memilih perkalian")
elif operasi == "4":
  print("User memilih pembagian")
elif operasi == "5":
  print("User memilih modulus")
elif operasi == "6":
  print("User memilih floor devision")
else:
  print("Tidak Valid")


if operasi == "1":
  hasil = bilangan1 + bilangan2
  print(f"Hasil operasi dari {bilangan1} + {bilangan2} = {hasil}")
elif operasi == "2":
  hasil = bilangan1 - bilangan2
  print(f"Hasil opersai dari {bilangan1} - {bilangan2} = {hasil}")
elif operasi == " 3":
  hasil = bilangan1 * bilangan2
  print(f"Hasil operasi dari {bilangan1} * {bilangan2} = {hasil}")
elif operasi == "4":
  hasil = bilangan1 / bilangan2
  print(f"Hasil operasi dari {bilangan1} / {bilangan2} = {hasil}")
elif operasi == "5":
  hasil = bilangan1 % bilangan2
  print(f"Hasil operasi dari {bilangan1} % {bilangan2} = {hasil}")
elif operasi == "6":
  hasil = bilangan1 // bilangan2
  print(f"Hasil operasi dari {bilangan1} //{bilangan2} = {hasil}")
else:
  print("Tidak Valid")