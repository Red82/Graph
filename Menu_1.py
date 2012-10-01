__author__ = 'red'
from Tkinter import  *

#Exit
def win_exit():
    root.destroy()

#Information about product
def win_about():
    win = Toplevel(root)
    win.title("Laboratory work")
    win.minsize(width=300, height=200)
    l = Label(win, text="This only a laboratory work..")
    l.pack()

#ChangeColor
def color_red():
    root.config(bg="red")
def color_green():
    root.config(bg="green")
def color_blue():
    root.config(bg="blue")

#ChangeSize
def size_small():
    root.config(width=500, height=500)
def size_large():
    root.config(width=700, height=400)

root = Tk()
root.title("My program")
root.minsize(width=300, height=200)

#Menu
m = Menu(root)
root.config(menu=m)

am = Menu(m)
m.add_cascade(label="File", menu=am)
am.add_command(label="About", command=win_about)
am.add_command(label="Exit", command=win_exit)

bm = Menu(m)
m.add_cascade(label="Color", menu=bm)
bm.add_command(label="Red", command=color_red)
bm.add_command(label="Green", command=color_green)
bm.add_command(label="Blue", command=color_blue)

cm = Menu(m)
m.add_cascade(label="Size", menu=cm)
cm.add_command(label="500x700", command=size_small)
cm.add_command(label="700x400", command=size_large)

root.mainloop()
