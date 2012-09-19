__author__ = 'red'
from Tkinter import *

root = Tk()
root.geometry("400x300")

#Frame1
fr_1 = Frame(root, bg='green', width=400,
            height=100, bd=20)
#Frame2
fr_2 = Frame(root, bg='darkgreen',
            width=200, height=80, bd=20)
#Text
txt = Entry(fr_2)
#Scale
sc = Scale(fr_1, from_=0, to=100,
            tickinterval=10, orient=HORIZONTAL,
            length=300)
#ScrollBar
tx = Text(root, width = 40, height = 5)
scr = Scrollbar(root, command=tx.yview)


fr_1.grid(row=0, column=0)
fr_2.grid(row=1, column=0)
txt.grid(row=0, column=0)
sc.grid(row=3, column=0)
tx.grid(row=5, column=0)
scr.grid(row=3, column=10)



root.mainloop()