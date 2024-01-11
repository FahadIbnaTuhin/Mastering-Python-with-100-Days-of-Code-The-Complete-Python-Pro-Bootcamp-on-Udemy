from turtle import Turtle, Screen, colormode
import random

tortoise = Turtle()
tortoise.speed("fastest")
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tortoise.color(random_color())
        tortoise.circle(100)
        # tortoise.left(size_of_gap)
        tortoise.setheading(tortoise.heading() + size_of_gap)


draw_spirograph(25)

screen = Screen()
screen.exitonclick()
