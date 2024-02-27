import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/hindi.csv")
    # records : to make every column is inside the first row separately
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
# print(data_dict)


def next_card():
    global current_card, flip_cancel
    window.after_cancel(flip_cancel)
    current_card = random.choice(data_dict)
    # print(current_card["Hindi"])
    canvas.itemconfig(card_title, text="Hindi", fill="black")
    canvas.itemconfig(card_word, text=current_card["Hindi"], fill="black")
    canvas.itemconfig(card_background, image=card_font_pic)
    flip_cancel = window.after(3000, func=flip_card)


def flip_card():
    # print(current_card)
    canvas.itemconfig(card_background, image=card_back_pic)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    data_dict.remove(current_card)
    print(len(data_dict))

    global data
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Learn Hindi")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_cancel = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_font_pic = PhotoImage(file="images/card_front.png")
card_back_pic = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_font_pic)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# This below line so that at the beginning it starts showing random thing
next_card()

window.mainloop()
