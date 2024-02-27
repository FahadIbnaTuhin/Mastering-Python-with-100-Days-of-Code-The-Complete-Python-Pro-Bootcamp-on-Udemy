from password_generator import password_generator
from tkinter import *
# first one import all the classes and constants
from tkinter import messagebox
# messagebox is another module of code
import pyperclip

FONT = ("Arial", 15, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    # (0, END) means delete everything from the index 0 to the end
    password_entry.delete(0, END)
    pwd = password_generator()
    password_entry.insert(0, pwd)
    pyperclip.copy(pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web, info, pwd = website_entry.get(), user_info_entry.get(), password_entry.get()

    if web == "" or info == "" or pwd == "":
        messagebox.showinfo(title="Missing Data", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askyesno(title=web, message=f"These are the details entered: \nEmail: {info}\n"
                                                       f"Password: {pwd}\nIs it okay? ")

        if is_ok:
            with open("data.csv", "a") as file:
                file.write(f"{web},{info},{pwd}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=80)

canvas = Canvas(width=200, height=200)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pic)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

user_info = Label(text="Email/Username:", font=FONT)
user_info.grid(column=0, row=2)

password = Label(text="Password:", font=FONT)
password.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

user_info_entry = Entry(width=52)
user_info_entry.insert(0, "fahadtuhin2@gmail.com")
user_info_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
generate_pwd_button = Button(text="Generate Password", command=generate_pwd)
generate_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
