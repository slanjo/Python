from turtle import Turtle

#PADDLE_MOVE_DISTANCE = 20
#PADDLE_START_POSITION = ((350,0), (-350, 0))

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
















#-------------------------------
#         INITIAL PADDLE CLASS
#-------------------------------
'''
class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_paddle()
    
    def create_paddle(self):
        for i in PADDLE_START_POSITION: 
            self.add_paddle(i) 

    def add_paddle(self, position):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.penup()
        self.paddle.setheading(90.0)
        self.paddle.shapesize(stretch_len=5, stretch_wid=1)
        self.paddle.setposition(position)
        self.paddle.color("white")
        self.paddle.speed("fastest")

#    def move(self):
#        self.paddle.fd(PADDLE_MOVE_DISTANCE)

    def up(self):
        self.paddle.fd(PADDLE_MOVE_DISTANCE) 

    def down(self):
        self.paddle.bk(PADDLE_MOVE_DISTANCE)
'''

