from tkinter import *
from turtle import width
root = Tk()

for i in range(5):
    root.columnconfigure(i, weight=5)
    tombol = Button(root, text="Tombol")
    tombol.grid(row=0, column=i, sticky=E+W) # membuat jadi dinamis

mainloop()