def turn_around():
    for i in range(3):
        turn_left()
def go_ahead():
   for i in range(3):
        move()
def repeat1():
    go_ahead()    
    turn_left()    
    go_ahead()
def repeat2():
    turn_around()
    move()
    turn_around()
for i in range(3):
    repeat1()
    repeat2()
repeat1()

