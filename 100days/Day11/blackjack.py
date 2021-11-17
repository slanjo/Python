import random
from os import system
from art import logo
print(logo)

def deal(current_card_list, cards, more):

    num_of_cards = len(cards)
    card = 0
    card = random.choice(cards)
    if card == 11 and sum(current_card_list) + 11 > 21:
        return 1 
    else:
        return card 

def totals(current_card_list):

    return sum(current_card_list)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0
more = True 
play = True

while play:

#### Terminate game
    again = input("Would you like to play a game of BlackJack? (Y/N): ").lower()
    if again == "n":
        play = False
        print("Thank you for playing!")

    else:
        another_card = True
        system('clear')
        print(logo)
        player_cards = []
        dealer_cards = []
        player_score = 0
        dealer_score = 0

#Player first two cards
        player_cards.append(deal(player_cards, cards, more))
        player_cards.append(deal(player_cards, cards, more))
        print(f"Your cards: {player_cards}, current score {sum(player_cards)}")

#Dealer first two cards
        dealer_cards.append(deal(dealer_cards, cards, more))
        dealer_cards.append(deal(dealer_cards, cards, more))
        print(f"Computer's first card: {dealer_cards[0]}")

        while another_card:

            one_more_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if one_more_card == 'n':
                player_score = sum(player_cards) 
                another_card = False

            else:
                player_cards.append(deal(player_cards, cards, more))
                player_score = sum(player_cards) 
                print(f"Your cards {player_cards}, current score: {player_score}")

            if dealer_score < 17:
                dealer_cards.append(deal(dealer_cards, cards, more)) 
                dealer_score = sum(dealer_cards) 

        if player_score == dealer_score:
            print(f"    Your final hand: {player_cards}, final score: {player_score}")
            print(f"    Computer's final hand: {dealer_score}, final score {dealer_score}")
            print("Draw")   

        elif player_score > 21:

            print(f"    Your final hand: {player_cards}, final score: {player_score}")
            print(f"    Computer's final hand: {dealer_score}, final score {dealer_score}")
            print("You went over. You lose")   

        elif dealer_score > 21: 
            print(f"    Your final hand: {player_cards}, final score: {player_score}")
            print(f"    Computer's final hand: {dealer_score}, final score {dealer_score}")
            print("You win!")   

        elif player_score > dealer_score:

            print(f"    Your final hand: {player_cards}, final score: {player_score}")
            print(f"    Computer's final hand: {dealer_score}, final score {dealer_score}")
            print("You win!")   
        

        elif player_score < dealer_score:

            print(f"    Your final hand: {player_cards}, final score: {player_score}")
            print(f"    Computer's final hand: {dealer_score}, final score {dealer_score}")
            print("You lose")   
            
