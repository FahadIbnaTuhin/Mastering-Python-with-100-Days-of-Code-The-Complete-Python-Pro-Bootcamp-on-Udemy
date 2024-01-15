from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.at_the_beginning()

    def at_the_beginning(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
        # if self.ycor() > FINISH_LINE_Y:
        #     return True
        # return False

