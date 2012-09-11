from Tkinter import *

can = Canvas(width=525, heigh=800, bg='white')
can.pack(expand=YES, fill=BOTH)
can.create_line(100, 100, 200, 200)
can.create_line(100, 200, 200, 300)


can.create_oval(10, 10, 200, 200, width=2, fill='red')
can.create_arc(200, 200, 300, 100)
can.create_rectangle(200, 200, 300, 300, width=2, fill='blue', outline='yellow')
a = can.create_line(0, 300, 150, 150, width=10, fill='green')

for i in range(1, 100, 10):
    can.create_line(0, i, 50, i)

photo= PhotoImage(file='c:\\111.gif')
can.create_image(300, 300, image=photo, anchor=NE)
can.move(a, 100, 500)

Lab = Label(can, background='blue',bd=5, text='Spam')
Lab.pack()
can.create_window(100, 100, window=Lab)
can.create_text(100, 300, text='Ham')

mainloop()
