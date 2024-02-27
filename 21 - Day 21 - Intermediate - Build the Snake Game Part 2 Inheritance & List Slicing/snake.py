from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)
        # return self.segments

    def add_segments(self, position):
        timmy = Turtle("square")
        timmy.penup()
        timmy.color("white")
        timmy.goto(position)
        self.segments.append(timmy)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[seg - 1].xcor()
            ycor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(xcor, ycor)
        self.segments[0].forward(MOVE_DISTANCE)
        # self.segments[0].left(90)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

