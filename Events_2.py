__author__ = 'red'
def resiz_1(event):
        fr.configure(width=100,height=100)

def resiz_2(event):
    fr.configure(width=300,height=300)

def resiz_3(event):
    fr.configure(width=500,height=500)

from Tkinter import *
root = Tk()

fr = Frame(root, width=500, height=500)
btn_1 = Button(root, text='1', width= 10)
btn_2 = Button(root, text='2', width= 10)
btn_3 = Button(root, text='3', width= 10)

fr.pack()
btn_1.pack()
btn_2.pack()
btn_3.pack()

btn_1.bind("<Button-1>", resiz_1)
btn_2.bind("<Button-1>", resiz_2)
btn_3.bind("<Button-1>", resiz_3)

root.mainloop()
