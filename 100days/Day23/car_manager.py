from turtle import Turtle
import random  
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup() 
        self.color(self.car_color())
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.new_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_color(self):
        for car_color in COLORS:
            return random.choice(COLORS)
    
    def move_car(self):
#        new_x = self.xcor() - self.car_speed
#        self.goto(new_x, self.ycor())
        self.fd(self.car_speed)

    def new_car(self):
        car_y = random.randint(-250, 250) 
        self.goto(300, car_y)
    
    def speed_inc(self):
        self.car_speed += MOVE_INCREMENT