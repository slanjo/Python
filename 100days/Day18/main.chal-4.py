import random
import turtle as t
import random as r
DIST = 30 
ANGLE = 90
THICK = 15

def walk(direction, my_turtle, my_screen):
#    my_turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    my_turtle.pencolor((random_color()))
    my_turtle.width(THICK)
    my_turtle.speed(10)
    print(f"{direction}")
    if direction == "lt":
        my_turtle.lt(ANGLE) 
        my_turtle.fd(DIST)
    elif direction == "fd":
        my_turtle.fd(DIST)
    elif direction == "rt":
        my_turtle.rt(ANGLE) 
        my_turtle.fd(DIST)
    else:
        my_turtle.bk(DIST)
    return

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

if __name__ == '__main__':
    my_turtle = t.Turtle()
    my_screen = t.Screen()
    my_screen.colormode(255)
    direction_list = ["lt", "rt", "fd", "bk"] 
    print(f"{random.choice(direction_list)}")

#    while not my_screen.exitonclick():
    while True: 
        walk(random.choice(direction_list), my_turtle, my_screen)
