print("====================================================")
data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('ayo D\'bacot')
print('g\'day, isn\'t it?')

# backlash
print("C:\\usr\\muhaemin")

# tab
print("muhaemin\t\t\tdan sidia, semakin jauhan")

# backspace
print("muhaemin \bsidia, bisa deketan")

# newline
print("kalimat pertama.\nkalimat kedua.")  # LF -> line feed -> unix, macos, linux
# CR -> carriage return -> commodore, acorn, lisp
print("kalimat pertama.\rkalimat kedua.")
# CRLF -> line feed carriage return -> dipakai oleh windows
print("kalimat pertama.\r\nkalimat kedua.")

# 3. String literal atau raw

# hati-hati
print('C:\new folder')  # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama  : Muhaemin
Kelas : 3 SD   
""")

# multiline literal string dan RAW
print(r"""
        Nama    : Muhemin
        Kelas   : 3 SD\new normal 
        Website : www.muhaemin.com/newID
        """)
