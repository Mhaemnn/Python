
from tkinter import *

warna = ['white','yellow','white','yellow','white','yellow']

r = 0
for c in warna:
    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1

mainloop()