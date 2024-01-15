from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.extend()

    # Detect collision with wall
    if (snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300
            or snake.segments[0].ycor() < -290):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
