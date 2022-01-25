from turtle import Turtle 
import random

class Ball(Turtle):
 
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.sleep_time = 0.1
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10 

    def move(self):
            new_x = self.xcor() + self.x_move 
            new_y = self.ycor() + self.y_move 
            self.goto(new_x, new_y) 
    
    def bounce_y(self):
        self.y_move *= -1
        self.sleep_time *= .9

    def bounce_x(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.goto((0, 0 ))
        self.bounce_x()
        self.sleep_time = 0.1
 