#imports
from tkinter import *
from tkinter import ttk

#functions
def open_file():
    file= f"{entry.get()}.{combobox.get()}"
    f = open(file, 'r')
    print(*f)

#window
win = Tk()
win.title("File opener")
win.geometry("300x300")

entry = ttk.Entry()
entry.pack(padx=8, pady= 8)

ext = ["txt", "html"]

combobox = ttk.Combobox(values=ext, state="readonly")
combobox.pack(padx=4, pady=4)

btn = ttk.Button(text="Open", command=open_file)
btn.pack()

win.mainloop()