from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Feeling Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # print(ball.distance(r_paddle), ball.xcor())
        ball.bounce_x()

    # When right side misses
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.l_point()

    # When left side misses
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
