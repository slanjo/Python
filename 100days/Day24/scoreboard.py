from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.highscore = self.read_high_score() 
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def read_high_score(self):
#Solution to the first lecture challenge
#       with open("~/Desktop/data.txt", "r") as f:
#Solution to the second lecture challenge for the main.py in /Users/slanjo/Projects/Python/100days/Day24
#       with open("../../../../Desktop/data.txt", "r")
        with open("data.txt", "r") as f:
            return int(f.read())

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        with open("data.txt", "w") as f:
            f.write(f"{self.highscore}")
        self.update_scoreboard()
#    def game_over(self):
#        self.goto(0, 0)
#        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
