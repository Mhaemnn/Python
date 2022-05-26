class Segitiga:

  def __init__(self, alas,tinggi) -> None:
      self.alas = alas
      self.tinggi = tinggi
      self.luas = 0.5 *  alas * tinggi


SegitigaBesar = Segitiga (100,80)

# akses varible alas, tinggi, dan luas dari luar kelas
print(f"alas: {SegitigaBesar.alas}")
print(f"tinggi: {SegitigaBesar.tinggi}")
print(f"luas: {SegitigaBesar.luas}")
