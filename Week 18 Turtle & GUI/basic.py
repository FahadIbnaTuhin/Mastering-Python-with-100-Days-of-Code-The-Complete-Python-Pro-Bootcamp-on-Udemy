from turtle import Turtle, Screen

tortoise = Turtle()
# tortoise.shape("turtle")
# tortoise.color("red")
# tortoise.forward(100)
# tortoise.right(90)

# for _ in range(4):
#     tortoise.right(90)
#     tortoise.forward(100)

for _ in range(5):
    tortoise.forward(10)
    tortoise.penup()
    tortoise.forward(10)
    tortoise.pendown()


screen = Screen()
screen.exitonclick()
