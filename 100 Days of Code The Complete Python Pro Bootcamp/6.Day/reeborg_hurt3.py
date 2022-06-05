
def turn_right():
    for i in range(3):
        turn_left()
def wall_around():
    turn_left()
    while wall_in_front():
        turn_left()
    for i in range(2):
        move()
        turn_right() 
    move()
    turn_left()
while front_is_clear():
    move()
    while wall_in_front():
        wall_around()
    if at_goal():
        done()