from art import logo, vs 
from game_data import data
import random
from os import system

def compare(follower_count_a, follower_count_b, u_choice):
    if follower_count_a > follower_count_b:
        if u_choice == 'a':
            return 'A'
    elif follower_count_a < follower_count_b:
        if u_choice == 'b':
            return 'B'
    else:
        return 'N'
    
again = True
current_score = 0
final_score = 0
print(logo)
print(vs)

comparator_a = random.choice(data)
comparator_b = random.choice(data)

print(f"Compare A: {comparator_a['name']}, a {comparator_a['description']}, from {comparator_a['country']}. ")
print(f"Against B: {comparator_b['name']}, a {comparator_b['description']}, from {comparator_b['country']}. ")
choice = input("Who has more followers? Type 'A' or 'B': ").lower()
compare_result = compare(comparator_a['follower_count'], comparator_b['follower_count'], choice)

while again:
#choose a random dictionary from game data file

    if  compare_result == 'A':
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        comparator_b = random.choice(data)

    elif compare_result == 'B':
        comparator_a = comparator_b
        comparator_b = random.choice(data)
        current_score += 1
        print(f"You're right! Current score: {current_score}")

    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        again = False

    if again == True:
        system('clear')
        print(logo)
        print(f"Compare A: {comparator_a['name']}, a {comparator_a['description']}, from {comparator_a['country']}. ")
        print(vs)
        print(f"Against B: {comparator_b['name']}, a {comparator_b['description']}, from {comparator_b['country']}. ")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        compare_result = compare(comparator_a['follower_count'], comparator_b['follower_count'], choice)

    
