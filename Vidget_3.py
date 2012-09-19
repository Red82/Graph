__author__ = 'red'
from Tkinter import  *

root = Tk()
root.geometry("600x600")

#Frames
fr1 = Frame(root, width=500, height=100, bg='darkred', bd=5)
fr2 = Frame(root, width=300, height=100, bg='green', bd=20)
fr3 = Frame(root, width=500, height=150, bg='darkblue', bd = 20)

#Text
e1 = Entry(fr2, width=10)

#Scale
sca1 = Scale(fr1, orient=HORIZONTAL, length=200, from_=0,
            to=1000, tickinterval=200, resolution = 100)

#Toplevel
win = Toplevel(root, relief=SUNKEN, bd=10, bg='lightblue')
win.title("Doter's window")
win.minsize(width=400,height=200)

fr1.pack()
fr2.pack()
fr3.pack()
e1.pack()
sca1.pack()


root.mainloop()