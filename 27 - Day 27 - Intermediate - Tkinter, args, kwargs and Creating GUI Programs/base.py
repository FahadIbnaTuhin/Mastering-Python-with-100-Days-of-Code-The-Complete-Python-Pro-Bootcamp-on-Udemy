from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)

# Label
my_label = Label(text="Hi", font=("Arial", 20, "bold"))
my_label.pack()
# my_label["text"] = "FAHAD"
my_label.config(text="Hello, World!")


def button_clicked():
    # print("I got clicked")
    inp = inputt.get()
    my_label.config(text=f"Hello, {inp}!")


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
inputt = Entry(width=10)
inputt.pack()


window.mainloop()
