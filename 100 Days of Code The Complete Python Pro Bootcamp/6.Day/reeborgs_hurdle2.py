
def turn_around():
    for i in range(3):
        turn_left()
#  at_goal is target I want to arrive my goal.
while not at_goal():
    move()
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()