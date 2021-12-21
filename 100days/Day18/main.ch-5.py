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
 
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(RADIUS)
        tim.setheading(tim.heading() + size_of_gap)
 
if __name__ == '__main__':
    tim = t.Turtle()
    my_screen = t.Screen()
    t.colormode(255)
    tim.speed("fastest")
 
#### MY SOLUTION ######
#    for i in range(0, 370, 10):
#        tim.pencolor(random_color())
#        tim.circle(RADIUS)
#        tim.setheading(i)
#    my_screen.exitonclick()
#### Angela's Solution
    draw_spirograph(5)
    my_screen.exitonclick()