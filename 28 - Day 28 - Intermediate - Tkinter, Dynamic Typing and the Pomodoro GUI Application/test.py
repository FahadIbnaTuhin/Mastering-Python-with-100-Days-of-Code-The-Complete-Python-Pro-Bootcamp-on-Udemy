from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
# Color are taken from: https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW)
photo = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=photo)
canvas.create_text(102, 130, text="00:00", fill="white", font=("Arial", 34, "bold"))
canvas.pack()

window.mainloop()
