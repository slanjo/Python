STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_DISTANCE = 20
from turtle import Turtle


class Snake:
 #        self.snake = snake
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.color("white")
            self.segments.append(new_segment)

    def move(self):

        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor() 
            new_y = self.segments[seg_num -1 ].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(FORWARD_DISTANCE)   

    def up(self, direction):
        self.segments[0].left(90)
        pass
    def down(self):
        pass
    def left(self):
        pass
    def right(self):
        pass