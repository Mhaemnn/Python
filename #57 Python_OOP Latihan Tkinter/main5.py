from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button

class MembuatTombol(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.tombol()

        self.parent.title("Membuat Tombol")
        self.pack(fill=BOTH, expand=1)

    def tombol(self):
        variabelTombol = Button(self, text="Ini Tombol")
        variabelTombol = Button(self, text="Exit", command=self.quit) # exit menggunakan fungsi commend=self.quit
        variabelTombol.place(x=50, y=50)

if __name__ == '__main__':
    root = Tk()
    root.geometry("250x150+300+300")
    app = MembuatTombol(root)
    root.mainloop()