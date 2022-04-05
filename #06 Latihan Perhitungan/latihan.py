
print("\n=============Latihan=============\n")


fahrenheit = float(input('Masukkan Suhu dalam Fahrenheit: '))
celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin, "Kelvin")


kelvin = float(input('Masukkan suhu dalam kelvin: '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit:", fahrenheit, "Fahrenheit")