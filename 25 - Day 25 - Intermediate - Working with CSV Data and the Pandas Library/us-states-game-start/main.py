import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
# turtle can work with only gif image format
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(730, 490)


def correct_guess(state, x, y):
    """write the state in the screen"""
    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto(x, y)
    state_turtle.write(state, False, "center", ("Arial", 8, "normal"))


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

correct = 0
correct_states = []
while correct < 51:
    answer_state = screen.textinput(f"{correct}/50 States Correct", "What's another state name? ").title()
    # print(answer_state)
    if len(data[data.state == answer_state]) != 0:
        row = data[data.state == answer_state]
        state_name = row.state.item()
        x_cor = row.x.item()
        y_cor = row.y.item()
        # print(f"{state_name}: {x_cor} & {y_cor}")
        correct_guess(state_name, x_cor, y_cor)
        correct += 1
        correct_states.append(state_name)

    else:
        print("Wrong")


print(correct_states)

screen.exitonclick()
