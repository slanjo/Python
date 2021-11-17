import random
from os import system
from art import logo
print(logo)

def deal(player_cards, cards, more):

    print("Dealing first two cards\n")
    num_of_cards = len(cards)
    if more:
        player_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))
    else:
        player_cards.append(random.choice(cards))

    print(player_cards)
    return sum(player_cards)


def deal_another():
    print("Dealing Another card\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0
more = False
play = True
total = 0
while play:

#### Terminate game
    again = input("Would you like to play a game of BlackJack? (Y/N): ").lower()
    if again == "n":
        play = False
        print("Thank you for playing!")

    else:
        another_card = True
        print(deal(player_cards, cards, more))
        print(deal(dealer_cards, cards, more)) 

        while another_card:
            one_more_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if one_more_card == 'n':
                another_card = False
            else:
                total += deal(player_cards,cards, more)

        



