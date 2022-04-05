#MENGAMBIL INPUTAN DARI USER

data  = input("Masukan Nama: ")
angka = int(input("Masukan Angka: "))
angka = float(input("Masukan Angka: "))
biner = bool(int(input("Masukan Bilangan Boolean: ")))
print("=============================================")


print("data = ", data, "type = ", type(data))
print("data = ", angka, "type = ", type(angka))
print("data = ", biner, "type = ", type(biner))


"""
1. str: data yang dimasukan pasti string
2. bool: untuk boolean harus di casting dulu ke int, lalu di casting ke boolean

"""