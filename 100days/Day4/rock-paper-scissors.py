rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Welcome to Slanjo's Rock-Paper-Scissors game")
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

ai_choice = random.choice(['0', '1', '2'])
ai_choice_int = int(ai_choice)
player_choice_int = int(player_choice)

if ai_choice_int == 0:
    print(f"ai chose ({rock})")
elif ai_choice_int == 1:
    print(f"ai chose ({paper})")
elif ai_choice_int == 2:
    print(f"ai chose ({scissors})")

if player_choice_int == 0:
    print(f"You chose ({rock})")
elif player_choice_int == 1:
    print(f"You chose ({paper})")
elif player_choice_int == 2:
    print(f"You chose ({scissors})")

result = [[['0','2'],['2','1'],['1','0']],[['1','2'],['2','0'],['0','1']]]
result_int = [[0,1],[0,2],[1,0], [1,2], [2,0],[2 , 1]]
final_score = [ai_choice, player_choice]
if ai_choice_int == player_choice_int:
    print("Result = DRAW")
elif final_score in result[0]: 
    print(f"YOU LOSE!\n")
elif final_score in result[1]:
    print(f"YOU WIN!\n")
