# Width and Multiline

# Data

data_nama = "Muhaemin Iskandar"
data_umur = 23
data_tinggi = 160.1
data_nomor_sepatu = 39

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print("\n"+10*"="+"Data String"+10*"=")
print(data_string)

# String multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+10*"="+"Data String"+10*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""
nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+10*"="+"Data String"+10*"=")
print(data_string)

# mengatur lebar
data_nama = "Muhaemin Iskandar"
data_tinggi = 160.17
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+10*"="+"Data String"+10*"=")
print(data_string)
