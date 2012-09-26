# First task
__author__ = 'red'
from Tkinter import *

def flags_on(event):
    ent.delete(0, END)
    s = ''
    if c1.get() == '1':
        s = c1.get()
    if c2.get() == '2':
        s +=c2.get()
    ent.insert(0, s)

def flags_off(event):
    ent.delete(0, END)
    s = ''
    if c1.get() == '0':
        s = c1.get()
    if c2.get() == '0':
        s += c2.get()
    ent.insert(0, s)

root = Tk()
root.title("EVANTS")
root.minsize(width=300, height=200)

#Text
ent = Entry(root, width=30)

#Flags
c1 = IntVar()
c2 = IntVar()
ch1 = Checkbutton(root,
    text="1-st flag",
    variable=c1, onvalue=1,
    offvalue=0)
ch2 = Checkbutton(root,
    text="2-d flag",
    variable=c2, onvalue=2,
    offvalue=0)

ent.bind("<Button-1>", flags_on)
ent.bind("<Button-3>", flags_off)


ch1.deselect()
ch2.deselect()

ent.pack()
ch1.pack()
ch2.pack()


root.mainloop()
