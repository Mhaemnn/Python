from textwrap import fill
from tkinter import Tk, Frame, Checkbutton, BOTH

class Contoh(Frame):
    def __init__(self,parent):
      Frame.__init__(self,parent)
      self.parent = parent

      self.initUI()
      self.BuatChackButton()

      def initUI(self):
        self.parent.title("Checkbutton")
        self.pack(fill=BOTH, expand=True)
        self.parent.geometry("250x150")

      def BuatCheckButton(self):
        cb = Checkbutton(self, text='ini checkbox 1')
        cb.place(x=50, y=50)

        cb = Checkbutton(self, text='ini checkbox 2')
        cb.place(x=50, y=50)
        
        cb = Checkbutton(self, text='ini checkbox 3')
        cb.place(x=50, y=50)
        
        cb = Checkbutton(self, text='ini checkbox 4')
        cb.place(x=50, y=50)

        cb = Checkbutton(self, text='ini checkbox 5')
        cb.place(x=50, y=50)

        cb = Checkbutton(self, text='ini checkbox 6')
        cb.place(x=50, y=50)


if __name__ == "__init__":
  root = Tk()
  app  = Contoh(root)
  root.mainloop()