__author__ = 'red'
from Tkinter import *

root = Tk()
root.title("Program")

#Canvas
c = Canvas(root, width=500, height=300,
            bg="red", cursor="pencil")
c.create_line(0,0,100,100, width=4)
c.create_line(100,100,300,100, width=4)
c.create_oval(0,0,300,200, width=4)
c.create_rectangle(200,200,300,300)
c.create_arc([160,230],[230,330],start=0,extent=140,fill="lightgreen")
c.create_text(150,150, text="QQQQQQQQQQ",
            font="Arial 16", anchor="e")


c.pack()

root.mainloop()

