__author__ = 'red'
from Tkinter import *
def mve(event):
    c.move(oval, 0, 20)
root = Tk()

c = Canvas(root, width=500, height=400)
oval = c.create_oval(30,10,130,80)
rect = c.create_rectangle(180,10,280,80, width=4)
trian = c.create_polygon(330,80,380,10,430,80,
            fill='grey80',outline="black")

x=10
while x < 400:
    c.move(rect, 0,2)
    c.delete(rect)

c.bind("<Button-1>", mve)

c.pack()

root.mainloop()