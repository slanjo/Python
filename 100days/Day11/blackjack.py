from os import system
from art import logo
print(logo)

def deal():
    print("Dealing first two cards\n")

def deal_another():
    print("Dealing Another card\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []
play = True

while play:

#### Terminate game
    again = input("Would you like to play a game of BlackJack? (Y/N): ").lower()
    if again == "n":
        play = False
        print("Thank you for playing!")

    else:
        another_card = True
        while another_card:
            one_more_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()




            if one_more_card == 'n':
                another_card = False
                print("I don't want any more cards") 
        



