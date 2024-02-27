import math
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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tik_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec, short_break_sec, long_break_sec = WORK_MIN * 60, SHORT_BREAK_MIN * 60, LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # If it is the 8th rep:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        # If it's the 2nd/4th/6th rep:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        # If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # print(count)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # count_sec = str(count_sec).zfill(2)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        tik = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            tik += "✔️"
        tik_label.config(text=tik)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

timer_label = Label(text="Timer", font=("Times New Roman", 35), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

tik_label = Label(fg=GREEN, font=(FONT_NAME, 10, "normal"))
tik_label.grid(column=1, row=4)

window.mainloop()
