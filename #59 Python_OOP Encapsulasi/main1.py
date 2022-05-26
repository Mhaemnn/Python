class Mobil:

  def __init__(self, merk) -> None:
      self._merk = merk


pajero = Mobil("Mitsubisi")

#tampikan _merk dari luar kelas
print(f"Merk: {pajero._merk}")