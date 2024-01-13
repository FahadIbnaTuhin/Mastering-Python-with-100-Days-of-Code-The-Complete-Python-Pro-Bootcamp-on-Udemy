from turtle import Turtle, Screen

timmy = Turtle()


def righttt():
    if not timmy.setheading(0):
        timmy.forward(10)


def lefttt():
    if not timmy.setheading(180):
        timmy.forward(10)


screen = Screen()

screen.listen()
screen.onkey(righttt, "Right")
screen.onkey(lefttt, "Left")

screen.exitonclick()
