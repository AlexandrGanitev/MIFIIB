import random
from tkinter import *

# from tkinter import ttk

root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
# canv.create_oval(50, 10, 150, 110, width=2)
# canv.create_oval(10, 120, 190, 190,
#               fill='grey70', outline='white')
# canv.create_text(100, 100,
#               text="Hello World,\nPython\nand Tk",
#               justify=CENTER, font="Verdana 14")
# canv.create_text(200, 200, text="About this",
#               anchor=SE, fill="grey")
colors = ['red', 'orange', 'yellow', 'green', 'blue']


def new_ball() :
    global x, y, r, ball
    canv.delete(ball)
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    r = 30
    ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(colors))


root.mainloop()
