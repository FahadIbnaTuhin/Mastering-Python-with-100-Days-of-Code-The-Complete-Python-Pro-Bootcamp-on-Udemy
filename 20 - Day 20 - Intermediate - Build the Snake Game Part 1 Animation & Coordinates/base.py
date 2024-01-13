from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
is_game_on = True

for position in starting_position:
    timmy = Turtle("square")
    timmy.penup()
    timmy.color("white")
    timmy.goto(position)
    segments.append(timmy)

while is_game_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(10)
    for seg in range(len(starting_position) - 1, 0, -1):
        xcor = segments[seg - 1].xcor()
        ycor = segments[seg - 1].ycor()
        segments[seg].goto(xcor, ycor)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()