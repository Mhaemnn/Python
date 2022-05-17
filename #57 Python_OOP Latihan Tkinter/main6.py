from tkinter import Tk, Frame, Checkbutton, BOTH

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()
        self.buatCheckButton()

    def initUI(self):
        self.parent.title("Checkbutton")
        self.pack(fill=BOTH, expand=True)
        self.parent.geometry("250x150")

    def buatCheckButton(self):
        cb = Checkbutton(self, text="ini checkbox 1")
        cb.place(x=50, y=50)

        cb = Checkbutton(self, text="ini checkbox 2")
        cb.place(x=50, y=70)

        cb = Checkbutton(self, text="ini checkbox 3")
        cb.place(x=50, y=90)

        cb = Checkbutton(self, text="ini checkbox 4")
        cb.place(x=50, y=110)

        cb = Checkbutton(self, text="ini checkbox 4")
        cb.place(x=50, y=130)

        cb = Checkbutton(self, text="ini checkbox 4")
        cb.place(x=50, y=150)

if __name__ == '__main__':
    root = Tk()
    app = Example(root)
    root.mainloop()