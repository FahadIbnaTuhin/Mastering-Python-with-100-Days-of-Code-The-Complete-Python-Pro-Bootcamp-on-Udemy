from tkinter import *

window = Tk()

r = Label(bg="red", width=20, height=5)
r.grid(column=0, row=0)

g = Label(bg="green", width=20, height=5)
g.grid(column=1, row=1)

b = Label(bg="blue", width=40, height=5)
b.grid(column=0, row=2, columnspan=2)

window.mainloop()
