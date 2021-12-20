import random
import turtle as t
import random as r

def draw_shape(num_of_sides):
    angls = 360 / num_of_sides 
    my_turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for _ in range(num_of_sides):
        my_turtle.forward(100)
        my_turtle.rt(angls)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    my_turtle = t.Turtle()
#    my_turtle.shape("arrow")
    my_screen = t.Screen()
    my_screen.colormode(255)
#    my_turtle.rt(90)
#    my_turtle.sety(10)
#    my_turtle.setx(-50)
    i = 3

    for num_of_sides in range(3, 11):
        draw_shape(num_of_sides)

    while not my_screen.exitonclick():
        pass