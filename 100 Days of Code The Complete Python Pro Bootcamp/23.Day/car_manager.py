from importlib.util import set_loader
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

random_positions = random.randint(0,300)
random_color = random.randint(0,5)
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS[random_color])
        self.shapesize(3,1)
        self.penup()
        self.goto(300,random_positions)
    
    def move(self):
        new_x = self.xcor() + STARTING_MOVE_DISTANCE
        self.goto(new_x,self.ycor())
