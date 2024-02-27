import random
from turtle import Turtle, colormode

timmy = Turtle()
colormode(255)
# Short: To work with rgb color, need to turn the mode on using colormode
# The colormode(255) function call sets the color mode for the turtle graphics window.
# the colormode function determines the range of RGB (Red, Green, Blue) values that can be used when specifying colors.


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


directions = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fastest")


def random_walk():
    timmy.forward(50)
    timmy.setheading(random.choice(directions))


while True:
    timmy.color(random_color())
    random_walk()
