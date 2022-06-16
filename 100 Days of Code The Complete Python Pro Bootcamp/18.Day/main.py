from turtle import Screen, Turtle
timmy_the_turtle  = Turtle()
# import turtle
# timmy_the_turtle = turtle.Turtle()

# import turtle as t
# tim = t.Turtle()

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()