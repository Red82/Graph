__author__ = 'red'
from Tkinter import *
def change_col(event):
    x = sc.get()
    if x == 0: fr.configure(bg='white')
    if x == 20: fr.configure(bg='red')
    if x == 40: fr.configure(bg='yellow')
    if x == 60: fr.configure(bg='green')
    if x == 80: fr.configure(bg='blue')
    if x == 100: fr.configure(bg='black')

root = Tk()
root.title('Color Scale')
root.minsize(width=300, height=200)

#Frame
fr = Frame(root, width = 100, height = 100,
        bg='blue')

#Scale
sc = Scale(root, orient = HORIZONTAL, length = 300,
        from_=0, to = 100, tickinterval=20,
        resolution=20)

sc.bind("<B1-Motion>", change_col)

fr.pack()
sc.pack()

root.mainloop()