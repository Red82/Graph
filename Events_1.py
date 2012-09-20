__author__ = 'red'
ls = ['green', 'red']
def color(event):
    fr.configure(bg=ls[0])
    ls[0], ls[1] = ls[1], ls[0]
def out(event):
    root.destroy()

from Tkinter import *
root = Tk()

fr = Frame(root, width=200, height=100)
btn = Button(root, text="Press")

fr.pack()
btn.pack()

fr.bind("<Enter>", color)
btn.bind("<Button-1>", out)

root.mainloop()