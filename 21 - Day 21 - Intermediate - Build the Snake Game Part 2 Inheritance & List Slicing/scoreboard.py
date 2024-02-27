from turtle import Turtle
ALIGN = "left"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-30, 275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGN, FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGN, FONT)

    def game_over(self):
        self.goto(-45, 0)
        self.write("GAME OVER", False, ALIGN, FONT)


