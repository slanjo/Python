# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year\n")
        else:
            print("Not a leap year(400)\n")
    else:        
        print("Leap year (divisible by 4 but not 100)\n")
else:
    print("Not a leap year(not div by 4)\n")
