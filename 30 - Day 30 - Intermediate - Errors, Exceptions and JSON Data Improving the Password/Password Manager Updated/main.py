from password_generator import password_generator
from tkinter import *
# first one import all the classes and constants
from tkinter import messagebox
# messagebox is another module of code
import pyperclip
import json

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
    new_data = {
        web: {
            "info": info,
            "password": pwd
        }
    }

    if web == "" or info == "" or pwd == "":
        messagebox.showinfo(title="Missing Data", message="Please make sure you haven't left any field empty.")
    else:
        try:
            # If file exists, loading and updating data
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            # If file not exist, creating a file and updating the first data
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # if try successfully happened, then this will happen
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            # it will always happen
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ----------------------------  Search  -----------------------------------------
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="WARNING", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=f"Information of {website} website", message=f"Your Details from {website}:\n"
                                f"Email/Username: {data[website]["info"]}\nPassword: {data[website]["password"]}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists")


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
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1)

user_info_entry = Entry(width=52)
user_info_entry.insert(0, "fahadtuhin2@gmail.com")
user_info_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

generate_pwd_button = Button(text="Generate Password", command=generate_pwd)
generate_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
