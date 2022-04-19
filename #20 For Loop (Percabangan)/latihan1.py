## Latihan membuat bilangan fibonaci dengan for
print(20*"="+"Fibonaci"+20*"="+"\n")
panjang = int(input("Masukkan panjang deret: "))

fibo = [0,1]

for i in range(2, panjang):
  angka1 = fibo[i -1]
  angka2 = fibo[i -2]
  angkaSelanjutnya = angka1 + angka2
  fibo.append(angkaSelanjutnya)

print(fibo)