from cProfile import label
import tkinter

root = tkinter.Tk()

def event():
    label = tkinter.Label(root, text="Python")
    label.pack()

label = tkinter.Label(root, text="Bahasa Pemrograman Yang Paling aku Sukai")
button = tkinter.Button(root, text="Click", command= event)

label.pack()
button.pack()
root.mainloop()