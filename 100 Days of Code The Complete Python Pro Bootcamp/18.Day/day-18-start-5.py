import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
tim.speed("fastest")
def draw_shape():
    tim.circle(100)
    tim.right(1)

for i in range(360):
    tim.color(random_color())
    draw_shape()
tim.hideturtle()
screen = t.Screen()
screen.exitonclick()