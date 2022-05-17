from tkinter import *
root = Tk()

# membuat teks dengan berbagai font memberi warna teks dan background
w = Label(root, text=" Teks ini menggunakan font 'Arial'", font='Arial', fg='red', bg='white').pack()
w = Label(root, text=" Teks ini menggunakan font 'verdana' dengan style 'italic'", font='Verdana 16 bold italic', fg='blue', bg='white').pack()
w = Label(root, text=" Teks ini menggunakan font 'Helvetica' dengan style 'italic", font='Helvetica 10 bold italic', fg='green', bg='white').pack()




mainloop()