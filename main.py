#imports
from tkinter import *
from tkinter import ttk

#functions
def open_file():
    f = open(entry.get(), 'r')
    print(*f)
#def selected(event):
#    selection = combobox.get()
#

#window
win = Tk()
win.title("File opener")
win.geometry("300x300")

entry = ttk.Entry()
entry.pack(padx=8, pady= 8)

#const = [".txt"]
#combobox = ttk.Combobox(values=const)
#combobox.pack(padx=6, pady=6)
#combobox.bind("<<ComboboxSelected>>", selected)

btn = ttk.Button(text="Open", command=open_file)
btn.pack()

win.mainloop()