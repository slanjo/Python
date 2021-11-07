


#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height > 120:
#    print("you can ride the rollercoaster")
#else:
#    print("You need a bit more before the ride")

## 🚨 Don't change the code below 👇
#number = int(input("Which number do you want to check? "))
## 🚨 Don't change the code above 👆
#
##Write your code below this line 
#if ( number % 2 == 0 ):
#    print("This is an even number")
#else:
#    print("This is an odd number")


#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height > 120:
#    print("you can ride the rollercoaster")
#    age = int(input("What is your age? "))
#    if age <= 12:
#        print("price is 5")
#    elif age <= 18:
#        print("price is 7")
#    else:
#        print("Price is 12")

#else:
#    print("You need a bit more before the ride")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickest are 5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are 7")
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
        print("Midlife crisis for free")
    else:
        print("Adult ticets are 12")
        bill = 12
    wants_photo = input("do you want a photo\n?")
    if wants_photo == "y":
        bill += 3
    print(f"your finall bill is {bill}")
    
else:
    print("You need a bit more before the ride")



