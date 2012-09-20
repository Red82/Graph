__author__ = 'red'
def output(event):
    s = ent.get()
    if s == "1":
        tex.delete(1.0,END)
        tex.insert(END,"1111111111111111111111111111111")
    elif s == "2":
        tex.delete(1.0,END)
        tex.insert(END,"2222222222222222222222222222222222222222222222")
    else:
        tex.delete(1.0,END)
        tex.insert(END,"33333333333333333333333333333333333333333333333333333333")

from Tkinter import *
root = Tk()

ent = Entry(root,width=1)
but = Button(root,text="Print")
tex = Text(root,width=20,height=3,font="12",wrap=WORD)

ent.grid(row=0,column=0,padx=20)
but.grid(row=0,column=1)
tex.grid(row=0,column=2,padx=20,pady=10)

but.bind("<Button-1>",output)

root.mainloop()
