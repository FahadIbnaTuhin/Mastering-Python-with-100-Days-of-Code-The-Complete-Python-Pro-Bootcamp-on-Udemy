import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(300, 150)
window.config(padx=50, pady=25)


def miles_to_km():
    user_input = float(entry1.get())
    ans = round(user_input * 1.609, 2)
    result.config(text=f"{ans}")


entry1 = tkinter.Entry(width=15)
entry1.focus()
entry1.insert(tkinter.END, string="0")
entry1.grid(column=1, row=0)

miles = tkinter.Label(text="miles", font=("Arial", 10, "bold"))
miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_to.grid(column=0, row=1)

result = tkinter.Label(width=15, text="0", font=("Arial", 10, "bold"))
result.grid(column=1, row=1)

km = tkinter.Label(text="Km", font=("Arial", 10, "bold"))
km.grid(column=2, row=1)

button = tkinter.Button(width=10, text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
