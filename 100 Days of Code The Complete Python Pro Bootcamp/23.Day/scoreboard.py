from turtle import Turtle
from typing_extensions import Self


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self)
        self.clear()
        self.goto(-270,270)
        self.write(self.score, align="center",font=FONT)

