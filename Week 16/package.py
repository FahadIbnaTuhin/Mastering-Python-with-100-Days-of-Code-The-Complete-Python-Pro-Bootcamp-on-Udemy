from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red", "blue")
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.exitonclick())