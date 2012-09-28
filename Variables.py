__author__ = 'red'
from Tkinter import *

def show(event):
    i = r.get()
    if i == 0:
        print ("1-st button on")
    elif i == 1:
        print ("2-nd button on")
    else:
        print ("3-d button on")

def press(event):
    x1 = c1.get()
    x2 = c2.get()
    x3 = c3.get()
    x = [x1, x2, x3]
    ls.delete(0, 2)
    for i in x:
        ls.insert(END,i)
    lb.configure(text=(x1 + ', ' + x2 + ', ' + x3))



root = Tk()
root.title("Variables")
root.minsize(width=300, height=200)

#Radiobuttons
r = IntVar()
r.set(1)
r_btn_1 = Radiobutton(root, text="1-st",
            variable = r, value = 0)
r_btn_2 = Radiobutton(root, text="2-nd",
            variable = r, value = 1)
r_btn_3 = Radiobutton(root, text="3-d",
            variable = r, value = 2)

#Button 1
btn_1 = Button(root, text="Print")
btn_1.bind("<Button-1>", show)

#Button 2
btn_2 = Button(root, text="Get values")
btn_2.bind("<Button-1>", press)

#ListBox
ls = Listbox(root, height=3)

#Label
lb = Label(root, text="Flags")

#CheckButton
c1 = StringVar()
c2 = StringVar()
c3 = StringVar()
ch_1 = Checkbutton(root, text="Circle",
            variable=c1, onvalue='Circle', offvalue='None')
ch_2 = Checkbutton(root, text="Triangle",
            variable=c2, onvalue='Triangle', offvalue='None')
ch_3 = Checkbutton(root, text="Rectangle",
            variable=c3, onvalue='Rectangle', offvalue='None')

r_btn_1.pack()
r_btn_2.pack()
r_btn_3.pack()
btn_1.pack()

ch_1.deselect()
ch_2.deselect()
ch_3.deselect()

ch_1.pack()
ch_2.pack()
ch_3.pack()
ls.pack()
btn_2.pack()
lb.pack()

root.mainloop()
