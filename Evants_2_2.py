__author__ = 'red'
from Tkinter import *

def ent(event):
        lbl.configure(text = txt.get())



root = Tk()
root.config(width=200, height=150)

lbl = Label(root, text="!!!!!!!!!")
txt = Entry(root, width=20, bg='grey')

lbl.pack()
txt.pack()

txt.bind("<Return>", ent)

root.mainloop()

