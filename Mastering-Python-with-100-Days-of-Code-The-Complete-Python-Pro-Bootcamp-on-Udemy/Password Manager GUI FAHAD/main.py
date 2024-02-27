import json
from password_generator import password_generator
import pyperclip
from tkinter import *
from tkinter import messagebox

BC = "dodger blue"
TEXT_COLOR = "yellow"
LABEL_FONT = ("Courier", 15, "bold")
ENTRY_FONT = ("Arial", 13, "normal")
BUTTON_FONT = ("COURIER", 8, "bold")


# --------------------------------------- Save All Info ---------------------------------------
def submit():
    site, username, pwd, url, note = (siteName_entry.get().title(), userName_entry.get(), password_entry.get(),
                                      url_entry.get(), note_entry.get())

    if site == "" or username == "" or pwd == "" or url == "":
        messagebox.showinfo(title="Missing Data", message="Please make sure you haven't left any field empty.")
    else:
        # If you want csv format
        with open("data.csv", "a") as file:
            file.write(f"{site},{url},{username},{pwd},{note}\n")

        # If you want json format
        new_data = {
            site: {
                "username": username,
                "password": pwd,
                "url": url,
                "note": note
            }
        }
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            siteName_entry.delete(0, END)
            password_entry.delete(0, END)
            url_entry.delete(0, END)
            note_entry.delete(0, END)
            siteName_entry.focus()


# --------------------------------------- Generate Password -----------------------------------
def generate_pwd():
    password_entry.delete(0, END)
    pwd = password_generator()
    password_entry.insert(0, pwd)
    pyperclip.copy(pwd)


# --------------------------------------  Search Button  ---------------------------------------
def search():
    site = siteName_entry.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Not Found", message="File Not Found")
    else:
        if site in data:
            messagebox.showinfo(title=site, message=f"Detail:\nSite: {site}\nUsername: {data[site]["username"]}\n"
                                                    f"Password: {data[site]["password"]}\nURL:{data[site]["url"]}\n"
                                                    f"Note: {data[site]["note"]}")
        else:
            messagebox.showerror(title="Not Found", message="There is no site name in this title.")


# --------------------------------------------- GUI -------------------------------------------
window = Tk()
window.title("Password Manager by FAHAD")
window.config(padx=45, pady=55, bg=BC)

canvas = Canvas(width=512, height=512, bg=BC, highlightthickness=0)
logo_pic = PhotoImage(file="pwd1.png")
canvas.create_image(256, 240, image=logo_pic)
canvas.grid(row=0, column=0, columnspan=3)


# Labels
siteName_label = Label(text="Site Name:", bg=BC, fg=TEXT_COLOR, font=LABEL_FONT)
siteName_label.grid(row=1, column=0)

userName_label = Label(text="Username:", bg=BC, fg=TEXT_COLOR, font=LABEL_FONT)
userName_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=BC, fg=TEXT_COLOR, font=LABEL_FONT)
password_label.grid(row=3, column=0)

url_label = Label(text="URL:", bg=BC, fg=TEXT_COLOR, font=LABEL_FONT)
url_label.grid(row=4, column=0)

note_label = Label(text="Note:", bg=BC, fg=TEXT_COLOR, font=LABEL_FONT)
note_label.grid(row=5, column=0)


# Entries
siteName_entry = Entry(width=35, font=ENTRY_FONT)
siteName_entry.focus()
siteName_entry.grid(row=1, column=1)

userName_entry = Entry(width=56, font=ENTRY_FONT)
userName_entry.insert(0, "fahadtuhin2@gmail.com")
userName_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35, font=ENTRY_FONT)
password_entry.grid(row=3, column=1)

url_entry = Entry(width=56, font=ENTRY_FONT)
url_entry.grid(row=4, column=1, columnspan=2)

note_entry = Entry(width=56, font=ENTRY_FONT)
note_entry.grid(row=5, column=1, columnspan=2)


# Buttons:
search_btn = Button(text="Search", font=BUTTON_FONT, width=25, command=search)
search_btn.grid(row=1, column=2)

generatePWDBtn = Button(text="Generate Password", font=BUTTON_FONT, width=25, command=generate_pwd)
generatePWDBtn.grid(row=3, column=2)

submitBtn = Button(text="Submit", width=71, font=BUTTON_FONT, command=submit)
submitBtn.grid(row=6, column=1, columnspan=2)

window.mainloop()
# Json:
# Site_Name, SearchBtn
# UserName
# Password, GeneratePWD
# url
# Notes
# ADD

# csv: name, url, username, password, note
