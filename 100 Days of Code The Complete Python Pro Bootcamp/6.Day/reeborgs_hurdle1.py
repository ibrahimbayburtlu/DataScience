def turn_around():
    for i in range(0,3):
        turn_left()

def repeat():
    for i in range(0,6):
        move()
        turn_left()
        move()
        turn_around()
        move()
        turn_around()
        move()
        turn_left()
repeat()
