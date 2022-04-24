# latihan pengulangan membuat segitiga

from itertools import count


sisi = 5

# 1.Menggunakan for 

# Dummy Variable
print(5*"="+"Menggunakan For"+5*"=")
count = 1
for i in range(sisi):
  print("*" * count)
  count += 1


# 2 . Menggunakan while
print(5*"="+"Menggunakan While"+5*"=")
count = 1
while True:
  print("*" * count)
  count += 1

  if count > sisi:
    break


