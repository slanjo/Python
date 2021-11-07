#print("Hello" + " " + "Angela")

#print("Day 1 - Python Print Function")
#print("The function is declared like this:")
#print("print('what to print')")

#Fix the code below 👇
#Day 1.2
#print("Day 1 - String Manipulation")
#print('String Concatenation is done with the "+" sign.')
#print('e.g. print("Hello " + "world")')
#print("New lines can be created with a backslash and n.")

#Day 1.3
#print(len('Hello ' + input("What is your name? ")))

#Day 1.4
#name = "Slanjo"
#print(name)
#name = "SlanjoB"
#
#print(name)
#name = input("what is your name? ")
#length = len(name) 
#print(length)

## 🚨 Don't change the code below 👇
#a = input("a: ")
#b = input("b: ")
## 🚨 Don't change the code above 👆
#
#####################################
##Write your code below this line 👇
#
#temp = a
#a = b
#b = temp 
#
#
##Write your code above this line 👆
#####################################
#
## 🚨 Don't change the code below 👇
#print("a: " + a)
#print("b: " + b)
##print(d)


#1. Create a greeting for your program.
print("Hello, this program will generate a band name for you\n")
#2. Ask the user for the city that they grew up in.
city = input("the city you grew up in:\n")
print("\n")
#3. Ask the user for the name of a pet.
pet = input ("what's the name of your first pet:\n")
#4. Combine the name of their city and pet and show them their band name.
print("\nYour band name could be: " + city + " " + pet)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
