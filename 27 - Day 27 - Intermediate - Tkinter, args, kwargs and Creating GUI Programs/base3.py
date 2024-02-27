from tkinter import *

window = Tk()
window.title("HELLO")
window.minsize(600, 600)
# my_label.place(x=0, y=0)
window.config(padx=200, pady=300)

# Label
label = Label(text="Hello")
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

# Button
button1 = Button(text="Click Me")
button1.grid(column=1, row=1)

# Another Button
button2 = Button(text="Click Me Again")
button2.grid(column=2, row=0)

entry = Entry()
entry.grid(column=3, row=2)

window.mainloop()
