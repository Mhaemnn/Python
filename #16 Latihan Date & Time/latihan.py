

nama = str(input("Masukan Nama\t\t: "))
gol = input("Golongan Kerja\t\t: ")
jam = int(input("Masukan Jam Kerja\t: "))
print("1. SMA \n2. D1 \n3. D3 \n4. S1")
golpen = input("Masukan Pendidikan \t:")
gajih = 2500000

##Menghitung Golongan Jabatan
if gol == "1":
  upah =0.05*gajih;
elif gol == "2":
  upah = 0.10*gajih;
elif gol == "3":
  upah = 0.15*gajih;
else:
  upah = 0;

##Menghitung Golongan Pendidikan
if golpen == "SMA":
  tunpen = 0.025*gajih;
elif gol == "D1":
  tunpen = 0.05*gajih;
elif gol == "D3":
  tunpen = 0.30*gajih;
elif gol == "S1":
  tunpen = 0.40*gajih;
else:
  tunpen = 0;

##Menghitung rumus
if jam > 8:
  lembur = jam -8
  hlembur = lembur * 3500
else:
  print("Tidak ada Golongan Pendidikan")

rumus = tunpen + upah + gajih + hlembur

print("\n")
print ("==================================================================")
print("")
print("\t\t\t Hitung Gajih Karyawan")
print("")
print ("==================================================================")
print("Nama \t\t\t\t:", nama)
print("Golongan Kerja \t\t\t:", gol)
print("Jumlah Jam Kerja \t\t:",jam)
print("Pendidikan \t\t\t:", golpen)
print(f"Gajih Pokok \t\t\t: {gajih:,}")
print(f"Tunjangan Jabatan \t\t: {upah:,}")
print("Tunjangan Pendidikan \t\t:", tunpen)
print(f"Honor Lembur \t\t\t: {hlembur:,}")
print(f"Total Gajih dan Tujangan \t: {rumus:,}")
