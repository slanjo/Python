import turtle as t
import random
RADIUS = 100

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
if __name__ == '__main__':

    tim = t.Turtle()
    my_screen = t.Screen() 
    t.colormode(255)
#    tim.pensize(2)
    tim.pencolor(random_color())
    tim.circle(RADIUS)
    tim.pencolor(random_color())
    tim.circle(RADIUS)
    tim.reset()
    tim.shape("circle")
    tim.shapesize(5,2)
    tim.tilt(30)
    tim.fd(50)
    tim.tilt(30)
    tim.fd(50)
    tim.tilt(30)
    tim.fd(50)
    tim.tilt(30)
    tim.fd(50)
    while not my_screen.exitonclick():
       my_screen()