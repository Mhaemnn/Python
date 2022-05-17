from tkinter import*

root = Tk()

w = Label(root, text='yellow', bg='yellow', fg='black')
w.pack(fill=X, padx=10, pady=3, side=LEFT)
w = Label(root, text='black', bg='black', fg='white')
w.pack(fill=X, padx=10, pady=3, side=LEFT)
w = Label(root, text='salmon', bg='salmon', fg='gray')
w.pack(fill=X, padx=10, pady=3, side=LEFT)
w = Label(root, text='red', bg='red', fg='white')
w.pack(fill=X, padx=10, pady=3, side=LEFT)


mainloop()

"""
keterangan:
  1. fill = untuk memenuhi window
  2. padx = horizontal padding 
  3. pady = vertikal padding di dalam window/luar widget
  4. ipadx = vertikal internal padding di dalam widget
  5. ipady = horizontal internal padding di dalam widget
  6. side  = mengatur posisi widget kanan or kiri
"""