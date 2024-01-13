from turtle import Turtle, Screen

timmy = Turtle()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_left():
    timmy.setheading(timmy.heading() + 10)


def turn_right():
    timmy.setheading(timmy.heading() - 10)


def clear():
    # Clear: remove all the art that you already did
    # Home: go back to home but if you don't penup, it will create a line to come back to home directly
    # to erase the line penup and pendown before and after home
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen = Screen()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")


screen.exitonclick()
