from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("Turtle")
        self.penup()
        self.start_position()
        self.heading(90)

    def start_position(self):
        self.goto(STARTING_POSITION)
    
    def go_up(self):
        self.forward(MOVE_DISTANCE)