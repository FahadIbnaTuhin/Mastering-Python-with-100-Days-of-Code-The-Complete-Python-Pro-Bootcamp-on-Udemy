import random
from turtle import Turtle, Screen

timmy = Turtle()
colors = ["lime", "dark violet", "red", "magenta", "cyan", "gold", "medium slate blue", "indigo"]


def draw(sides):
    angle = 360 / sides
    for _ in range(i):
        timmy.right(angle)
        timmy.forward(100)


for i in range(3, 11):
    timmy.color(random.choice(colors))
    draw(i)

screen = Screen()
screen.exitonclick()
