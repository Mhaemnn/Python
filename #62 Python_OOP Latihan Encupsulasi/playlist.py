print(26 * "=" + "Latihan Encupsulasi" + 26 * "=")

class playlist:
  def __init__(self,daftar_lagu) -> None:
    self.daftar_lagu = daftar_lagu
    self.current_posistion = 0

    def __switch_to_song(self,to_index):
      last_pos = len(self.daftar_lagu) - 1
      if to_index > last_pos : # geser kelagu lagu
        self.current_posistion = 0
      elif to_index < 0: # geser ke lagu akhir
        self.current_position = last_pos
      else:
        self.current_posistion = to_index
      lagu = self.daftar_lagu [self.current_position]
      print("Mumatar: {} oleh {}".format(lagu.judul, lagu.penyanyi))


      def play_first_song(self):
        self.__switch_to_song(0)

      def play_last_song(self):
        self.__switch_to_song(last_pos)

      def play(self):
        self.__switch_to_song(self.current_positiond)

      def play_next_song(self):
        self.__switch_to_song(self.current_position +1)

      def play_prev_song(self):
        self.__switch_to_song(self.current_position -1)