from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.tally_l = 0
        self.tally_r = 0
        self.penup()
        self.goto(-110, 250)
        self.shape(name=None)
        self.color("white")
        self.hideturtle()
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.clear() 
        self.write(f"{self.tally_l}            {self.tally_r}", False, align='left', font=("Courier", 44, "normal")) 

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("Arial", 24, "normal"))

    def update_score(self, player_tag):
        if player_tag == 1:
            self.tally_l += 1
        elif player_tag == 2:
            self.tally_r += 1
        self.draw_scoreboard()
