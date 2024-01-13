import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "orange", "purple", "pink"]
y_positions = [-90, -50, -10, 30, 70, 110]
all_turtle = []
game_on = False


for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-210, y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
