# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

# angka = 0

# while angka < 5:
# 	angka += 1

# 	if angka == 3:
# 		pass # ini tidak akan dieksekusi

# 	print(angka)

# continue




ankga = 10

print(f"ankga sekarang -> {ankga}")

while ankga < 5:
    ankga += 1
    print(f"ankga sekarang -> {ankga}")  # aksi 1

    if ankga == 3:
        print("nice!")
        continue  # akan membuat loop meloncat ke step selanjutnya

    print("whassup!")  # aksi 2

print("Pinish!")
