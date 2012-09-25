__author__ = 'red'
from Tkinter import *
def send(event):
    txt = ent.get()
    lbl.configure(text=txt)
def ext(event):
    root.destroy()


root = Tk()
root.minsize(width=300, height=200)

ent = Entry(root)
lbl = Label(root)

ent.bind("<Return>", send)
root.bind("<Control-q>", ext)

ent.pack()
lbl.pack()

root.mainloop()