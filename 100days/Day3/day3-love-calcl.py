# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
name3 = name1 + name2
true_total = 0  #acumulate the "true" letters count in a name
love_total = 0  #acumulate the "love" letters count in a name

total = 0 # used to acumulate the letter counts
#use count and lower 

true_total = name3.count('t') + name3.count('r') + name3.count('u') + name3.count('e')  
love_total = name3.count('l') + name3.count('o') + name3.count('v') + name3.count('e')
print(f"Your score is {true_total}{love_total}\n")

total = str(true_total) + str(love_total)
print(total)

#For Love Scores less than 10 or greater than 90, the message should be:
if int(total) < 10 or int(total) > 90:
    print(f"Your score is {total}, you go together like coke and mentos.\n")

#For Love Scores between 40 and 50, the message should be:
elif int(total) >= 40 and int(total) <= 50:
    print(f"Your score is {total} you are alright together.")

#Otherwise, the message will just be their score. e.g.:
else:
    print(f"Your score is {total}\n") 


