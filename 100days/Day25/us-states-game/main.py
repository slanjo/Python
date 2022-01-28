"""
-Convert the guess to Title case
-Check if the guess is among the 50 states
-Write correct guesses onto the map
-usa a loop to allow the user to keep guessing
-Record the correct guesses in a list
-Keep track of the score
"""
import turtle
import pandas
CORRECT_GUESSES = []

def check_guess(answer, data):
    #if correct append a guess to correct_guesses list
    state_list = data["state"].to_list()
    print(data[data.state == answer])
    if answer in state_list:
        return True 
    else:
        return None

def write_guess(df_row, answer):
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    coordinates = (int(df_row["x"]),int(df_row["y"]))
   
    print(f"WRITE ROW \n {row}")
    CORRECT_GUESSES.append(answer)
    print(type(row))
    state.goto(coordinates)
    state.write(answer, align='left', font=('Title', 8, 'normal'))

def update_score():
    pass

if __name__ == '__main__':
    data = pandas.read_csv("~/Projects/Python/100days/Day25/us-states-game/50_states.csv")
    states = data["state"].to_list()
    screen = turtle.Screen()
    screen.title(" U.S. States Game")
    image = "/Users/slanjo/Projects/Python/100days/Day25/us-states-game/blank_states_img.gif"
#    screen.setup(760, 500)
    screen.addshape(image)
    turtle.shape(image)

    game_on = True
    while len(CORRECT_GUESSES) < 50: 

        answer_state = screen.textinput(title=f"{len(CORRECT_GUESSES)}/50 States Correct", prompt="What's another state's name? ")
        row = data[data.state == answer_state]
        print(f"MAIN ROW {row}")
        if check_guess(answer_state, data):
            if answer_state in CORRECT_GUESSES:
                pass
            else:
                write_guess(row, answer_state)
        else:
            print("NO SUCH STATE") 

        #turtle.mainloop()
        #screen.exitonclick()
    