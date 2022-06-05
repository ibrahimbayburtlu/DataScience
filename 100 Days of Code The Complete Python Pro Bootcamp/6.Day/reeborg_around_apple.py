for i in range(4):
    for i in range(9):
        move()
        if object_here("apple"):
            take("apple")
    turn_left()