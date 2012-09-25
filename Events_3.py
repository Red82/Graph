__author__ = 'red'
from Tkinter import *
def b1(event):
    root.title("Left Button")
def b3(event):
    root.title("Right Button")
def move(event):
    root.title("Mouse moves")

root = Tk()

root.bind("<Button-1>", b1)
root.bind("<Button-3>", b3)
root.bind("<Motion>", move)

root.mainloop()