from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.tally = 0
        self.penup()
        self.goto(-50, 280)
        self.shape(name=None)
        self.color("white")
        self.hideturtle()
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.clear() 
        self.write(f"SCORE:  {self.tally}", False, align='left', font=("Arial", 14, "normal")) 

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.tally += 1
        self.draw_scoreboard()
