__author__ = 'red'
from Tkinter import *

root = Tk()
#Knopka
btn = Button(root,
            text="This is button",
            width=15,
            height=20,
            bg="Green", fg="Red")

#Metka
lbl = Label(root,
            text="This is label",
            width=5,
            height=1,
            bg="White")

#Tekstovoe pole
txt = Text(root,
            font="Arial 14",
            width=40,
            height=1)

#RadioKnopki
var = IntVar()
var.set(1)

rad_btn1 = Radiobutton(root,
            text="1",
            variable=var, value=1)
rad_btn2 = Radiobutton(root,
            text="2",
            variable=var, value=2)
rad_btn3 = Radiobutton(root,
            text="3",
            variable=var, value=3)

#Flags
c1 = IntVar()
c2 = IntVar()
ch_btn1 = Checkbutton(root,
            text="1-st flag",
            variable=c1, onvalue=1,
            offvalue=0)
ch_btn2 = Checkbutton(root,
            text="2-d flag",
            variable=c2, onvalue=1,
            offvalue=0)

#Spiski
spisok = ['Linux', 'Mac', 'Windows']
spis = Listbox(root, selectmode=SINGLE, height=5)
for i in spisok:
    spis.insert(END , i)


btn.pack()
lbl.pack()
txt.pack()
rad_btn1.pack()
rad_btn2.pack()
rad_btn3.pack()
ch_btn1.pack()
ch_btn2.pack()
spis.pack()

root.mainloop()
