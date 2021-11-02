number = 7
user_input = input("Would  you like to play? (Y/n) ")

while True:
    user_input = input("Would  you like to play? (Y/n) ")
    user_number = int(input("Guess our number: "))
    if user_number == number: 
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")


