import tkinter

# bisa menggunakan main_window atau root
main_window = tkinter.Tk()  # Tk ini adalah object

label1 = tkinter.Label(main_window, text='label1')
label2 = tkinter.Label(main_window, text='label2')

tombol1 = tkinter.Button(main_window, text='kirim')
tombol2 = tkinter.Button(main_window, text='selesai')

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_window.mainloop()

"""
1. OOP itu bisa sharing dengan orang lain dan bisa menggunakanya lagi
2. kalau ada package huruf pertama nya besar itu adalah calss
3. diPython setiap class huruf pertama nya besar contoh: Label
4. gimana dengan yang, pack()# ini adalah method
"""
