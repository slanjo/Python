print(5==5)

# Comparisons >, <, >=, <=, ==, !=

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]


print(friends == abroad)
print(friends is abroad) #checks if the two items are exactly the same thing


day_of_week = input("What is the day of the week today? ").lower()


if (day_of_week) == "monday":
    print("Have a great start to your week")
elif day_of_week == "tuesday":
    print("It's Tuesday.")
else: 
    print("Full speed ahead!")

