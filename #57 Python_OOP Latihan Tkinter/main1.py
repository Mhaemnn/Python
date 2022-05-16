from tkinter import Tk, Frame
class MengubahJudul(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,)

        self.tampilan = parent

        self.initUI()

    def initUI(self):
        self.tampilan.title("Program tkinter")


if __name__ == '__main__':
    root = Tk()
    app = MengubahJudul(root)
    root.mainloop()