from turtle import Turtle
FONT = ("Courier", 24, "normal")
TEXT = "Level 1"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.level = 1
        self.write("Level %s" % self.level, font=FONT)

    def game_over(self):
        self.goto(-70, 0)
        self.write("Game Over", font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.write("Level %s" % self.level, font=FONT)
