__author__ = 'red'
from Tkinter import *

#New button class
class ButtonSend:
    def __init__(self):
        self.btn = Button(root,
                        text='Send',
                        width=12, height=2,
                        bg="Light Blue")
        self.btn.bind("<Button-1>", self.btn_send)
        self.btn.pack()
    def btn_send(self,event):
        print('Send Send Send')

root = Tk()

#RadioButtons
var = IntVar()
var.set(1)
rad_btn0 = Radiobutton(root,
            text='0 - 10',
            variable = var, value=1)
rad_btn1 = Radiobutton(root,
            text='11 - 20',
            variable = var, value=2)
rad_btn2 = Radiobutton(root,
            text='21 - 30',
            variable = var, value=3)
rad_btn3 = Radiobutton(root,
            text='31 - 40',
            variable = var, value=4)

#CheckButtons
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
ch0 = Checkbutton(root,
            variable = c1, onvalue=1, offvalue=0,
            bg='Red', text='RED')
ch1 = Checkbutton(root,
            variable = c2, onvalue=1, offvalue=0,
            bg='Blue', text='BLUE')
ch2 = Checkbutton(root,
    variable = c3, onvalue=1, offvalue=0,
    bg='Green', text='GREEN')
ch3 = Checkbutton(root,
    variable = c4, onvalue=1, offvalue=0,
    bg='Yellow', text='YELLOW')

#Label 1
lbl = Label(root,
            text="Your adress",
            font='Arial 12',
            bg='White')

#Label 2
lbl_1 = Label(root,
    text='Comments',
    font='Arial 12')

#Label 3
lbl_2 = Label(root,
            text='How much?',
            font='arial 14')
#Label 4
lbl_3 = Label(root,
            text='What color?',
            font='Arial 14')

#Text
txt = Entry(root,
            width=20)

#Text
txt_1 = Text(root,
            width=25,
            heigh=6,
            wrap=WORD)



lbl.pack()
txt.pack()
lbl_1.pack()
txt_1.pack()
btn = ButtonSend()
lbl_2.pack()
rad_btn0.pack()
rad_btn1.pack()
rad_btn2.pack()
rad_btn3.pack()
lbl_3.pack()
ch0.pack()
ch1.pack()
ch2.pack()
ch3.pack()


root.mainloop()
