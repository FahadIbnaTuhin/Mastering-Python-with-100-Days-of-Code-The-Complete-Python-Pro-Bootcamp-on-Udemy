import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
# turtle can work with only gif image format
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(730, 490)

# Google: get x y coordinates on click python turtle
# def get_mouse_click_coor(x, y):
#     # turtle.onscreenclick(None)
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# # mainloop: alternative way to keeps the screen open even though our code has finished runnign
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
# print(all_state)
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(f"{len(guessed_state)}/50 States Guessed",
                                    "What's another state name? ").title()

    if answer_state == "Exit":
        missing_states = []
        for c_state in all_state:
            if c_state not in guessed_state:
                missing_states.append(c_state)
                # with open("learn.csv", "a") as file:
                #     file.write(c_state + "\n")
        # print(missing_states)
        forgotten_state = pandas.DataFrame(missing_states)
        # print(forgotten_state)
        forgotten_state.to_csv("learn.csv")
        break

    if answer_state in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # item(): Returns the first element
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        guessed_state.append(answer_state)

