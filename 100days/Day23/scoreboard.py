from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto((-210, 260))
        self.shape(name=None)
        self.hideturtle()
        self.draw_scoreboard()
    
    def draw_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} ", False, align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.draw_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)        
        self.write("GAME OVER", False, align="center", font=FONT)