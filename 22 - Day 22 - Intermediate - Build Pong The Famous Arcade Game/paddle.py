from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        # Height: 100 & Width: 20 | Normal turtle size 20x20 | Then here 100 / 20 = 5
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(cordinate)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

