import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape():
    tim.forward(random.randint(-10,10))
    tim.right(random.randint(-360,360))
    tim.speed("fastest")

while True:
    tim.color(random.choice(colours))
    draw_shape()
screen = t.Screen()
screen.exitonclick()