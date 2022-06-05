
put("token")
def turn_around():
    for i in range(3):
        turn_left()

while front_is_clear():
    move()
    if wall_in_front():
        turn_left()
    if right_is_clear():
        turn_around()
    if object_here("token"):
        done()