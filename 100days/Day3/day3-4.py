# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3

if size == "S":
    print("Small Pizza: $15\n")
    bill = 15
elif size == "M":
    print("Medium Pizza: $20\n")
    bill = 20
elif size == "L":
    print("Medium Pizza: $20\n")
    bill = 25
else:
    print("you must make a Pizza size selection: S, M, or L\n")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
        print("Pepperoni for small Pizza: +$2")
    else:
        print("Pepperoni for a Medium or Large Pizza: +$3")
        bill += 3

if extra_cheese == "Y":
    bill += 1
    print("Extra Chese for any size Pizza: +$1")

print(f"Your finall bill is: {bill}")
