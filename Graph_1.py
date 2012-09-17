__author__ = 'red'
from Tkinter import  *

class Btn_print:
    def __init__(self):
        self.btn = Button(root)
        self.btn["text"] = "Print"
        self.btn.bind("<Button-1>",self.printer)
        self.btn.pack()
    def printer(self, event):
        print("Hello world")

root = Tk()
Btn = Btn_print()
root.mainloop()
