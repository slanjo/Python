from turtle import Turtle, Screen
import time


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    starting_position = [(0, 0), (-20, 0), (-40, 0)]
    segments = []
    for position in starting_position:
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        segments.append(new_segment)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        for seg_num in range(len(segments) -1, 0, -1):
            new_x = segments[seg_num - 1].xcor() 
            new_y = segments[seg_num -1 ].ycor()
            segments[seg_num].goto(new_x, new_y)

        segments[0].forward(20)   
        segments[0].left(90)
#   korni_1 = Turtle(shape="square") 
#   korni_1.color("white", "white") 
#   korni_2 = Turtle(shape="square") 
#   korni_2.color("white", "white") 
#   korni_2.setposition(korni_1.xcor() - 20, 0.0)
#   korni_3 = Turtle(shape="square") 
#   korni_3.color("white", "white") 
#   korni_3.setposition(korni_2.xcor() - 20, 0.0)


    screen.exitonclick()