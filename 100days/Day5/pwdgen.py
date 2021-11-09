#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
usr_input_list = [nr_letters, nr_numbers, nr_symbols]
pwd_len = nr_letters + nr_symbols + nr_numbers
#char_type stores a type of char we're genning next
#0 = letter, 1 = num, 2 = symbol
char_type = [0, 1, 2]
print(f"User input = {usr_input_list}=\npassword should be {pwd_len} characters long")
lozinka = ' ' 
i = 0
#Loop over the total requested password length
#for i in range(0, pwd_len): !!!!!FOR LOOPS DON"T WORK THE SAME AS C!!!!  IT IS NOT POSSIBLE
#TO ADJUST THE ITERATION VARIABLE INSIDE THE FOR LOOP IN PYTHON. 
while i < pwd_len:
#Pick a random character type, i.e. a letter or a num or a symbol

    print("==========>>>>>Entered main loop")
    j = random.randint(0, 2)
    print(f"'J' == {j}'     ''I ==== ' {i}")
    k = False
    if sum(usr_input_list) > 0: 
        print(f"Entered main 'IF'>>>>'J'=={j}")
        if j == 0 and usr_input_list[0] > 0:
            print("entered letters 'if'")
            lozinka = lozinka + random.choice(letters)
            usr_input_list[0] -= 1
            k = True
        if (j == 1 and usr_input_list[1] > 0):
            print(f"Entered numbers")
            lozinka += random.choice(numbers)
            usr_input_list[1] -= 1
            k = True
        if (j == 2 and usr_input_list[2] > 0):
            print(f"Entered symbols")
            lozinka += random.choice(symbols)
            usr_input_list[2] -= 1
            k = True 
    if k == False:
        i -= 1
    i += 1


print(f"Generated password: {lozinka}")
print(usr_input_list)
