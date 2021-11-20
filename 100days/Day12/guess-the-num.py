
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
#################
from art import logo
import random

def guess_num(player_input):
    if player_input == 10:
        print("You Win")

def randomize_number():
    return random.randint(0, 100)

print(logo)
secret_number = randomize_number()
select_difficulty = ""
player_guess = -1
select_difficulty = input("Choose a difficulty. Type 'easy' or hard': ").lower()
attempts = 0
won = False 
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(f"Psst, the correct answer is {secret_number}")


if select_difficulty == "hard":
    print("You have 5 attempts remaining to guess the number")
    attempts = 5
elif select_difficulty == "easy":
    print("You have 10 attempts remaining to guess the number")
    attempts = 10


while attempts > 0: 
    player_guess = int(input("Make a guess: "))
    if player_guess == secret_number:
        print(f"You got it! The answer was {secret_number}.")
        attempts = 0
        won = True
    elif player_guess > secret_number:
        attempts-=1
        print(f"Too low.\nGuess again.\nYou have {attempts} attampts to guess the number! ")
    elif player_guess < secret_number:
        attempts-=1
        print(f"Too high.\nGuess again.\nYou have {attempts} to guess the number! ")
if won == False:
    print("You've run out of guesses, you lose.i\nRestart the program to play again")
else:
    print("Restart the program to play again.")
