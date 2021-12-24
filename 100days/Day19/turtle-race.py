from turtle import Turtle, Screen
import random
is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
lista_kornjaci = []
ipsilon = -120

for kornjaca in colors:
    color = kornjaca
    kornjaca = Turtle(shape="turtle")
    kornjaca.color(color)
    kornjaca.penup()
    kornjaca.goto(x=-230, y=ipsilon)
    lista_kornjaci.append(kornjaca)
    ipsilon += 50

if user_bet:
    is_game_on = True

while is_game_on:
    for kornjaca in lista_kornjaci:
        kornjaca.forward(random.randint(0, 10))
        if kornjaca.xcor() >= 230:
            is_game_on = False
            winning_color = kornjaca.pencolor()
            print(f"The winner is {kornjaca.pencolor()} turtle!")
            if user_bet == winning_color:
                print("You've won!") 
            else:
                print("You loose")

screen.exitonclick()