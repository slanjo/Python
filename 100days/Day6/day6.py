print("Hello")
num_char = len("Hello")

print(num_char)

def my_function():
    print("Hello")
    print("bye")
            
my_function()



#ROBOT
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#
#turn_right()
#turn_right()
#turn_right()
#
#move()
#turn_right()
#move()
#turn_right()
#move()
#turn_right()
#move()
#----------------------------
#REBORG JUMP CHALLENGE
#----------------------------
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#
#def jump():
#    move()
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()
#
#for step in range(6):
#    jump()
#============================
#reborg while loop hurdles 3
#============================
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#
#def jump():
##   move()
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()
#
#while not at_goal():
#    if wall_in_front():
#        jump()
#    if front_is_clear():
#        if not at_goal():
#            move()




#============================
#reborg while loop hurdles 4
#============================

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if wall_in_front():
        turn_left()
        if wall_in_front():
            turn_left()
            if wall_in_front():
                turn_left()
                if front_is_clear():
                    turn_left()
                    move()
    else:
        turn_right()
        move()
    while front_is_clear() and wall_on_right():
        move()
    if front_is_clear() and right_is_clear():
        turn_right()
        move()
        turn_right()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#============================
#reborg while loop hurdles 4 THEIR SOLUTION
#============================
def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#MAZE SOLUTION

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()




