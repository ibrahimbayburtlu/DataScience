put("token")

while front_is_clear():
    move()
    if wall_in_front():
        turn_left()
    if object_here("token"):
        done()
        
        