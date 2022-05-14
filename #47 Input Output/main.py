"""
## INPUT OUTPUT FILE PYTHON
# membuat file text
  1. w  = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibautkan file bar
  2. r  = read mode / hanya membaca
  3. a  = appendding mode / menambahkan file di akhir baris
  4. r+ = write and read mode
"""

# write mode
file1 = open("data.txt", "w")
file1.write("ini adalah data text dibuat menggunakan python3")
file1.write("\nini adalah baris kedua")
file1.close()

#read mode
file2 = open("data.txt", "r")
print(file2.read())


#appendding mode
file3 = open("data.txt","a")
file3.write("\ndata menggunakan appendding")
file3.close()

# write and read mode
