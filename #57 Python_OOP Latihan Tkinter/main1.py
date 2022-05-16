from tkinter import BOTH, Tk, Frame


class MengubahJudul(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='salmon')

        self.tampilan = parent

        self.initUI()

    def initUI(self):
        self.tampilan.title("Program tkinter")
        self.pack(fill=BOTH, expand=1)
        self.tampilan.geometry("250x150+300+300")


if __name__ == '__main__':
    root = Tk()
    app = MengubahJudul(root)
    root.mainloop()




