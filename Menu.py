# Rabota s menu
__author__ = 'red'
from  Tkinter import *
def new_win():
    win = Toplevel(root)
def close_win():
    root.destroy()
def about():
    win = Toplevel(root)
    lab = Label(win, text="This is only a program!")
    lab.pack()


root = Tk()
root.title("Menu")
root.minsize(width=300, height=200)
root.maxsize(width=500, height=400)

m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Open")
fm.add_command(label="New", command=new_win)
fm.add_command(label="Save")
fm.add_command(label="Quit", command=close_win)

nfm = Menu(fm)
fm.add_cascade(label="Import", menu=nfm)
nfm.add_command(label="Image")
nfm.add_command(label="Text")


hm = Menu(m)
m.add_cascade(label="Help", menu=hm)
hm.add_command(label="Help")
hm.add_command(label="About us", command=about)



root.mainloop()
