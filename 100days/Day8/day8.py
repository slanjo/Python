# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.



#def greet(some_name):
#    print(f"{some_name} You're inside the function now")
#    print("You're still inside the function ")
#    print("Still inside... ")


#name = "Sanjin"
#greet(name)


#Functions with more than one line input
def greet_with(name, where_from):
    print(f"{name} where you from? \n...\n...")
    print(f"{where_from}?! Nice!")

greet_with(where_from = "Sanjin", name="Croatia")
print("#" * 80)
key1 = "Mestar"
key2 = "Bosna"


greet_with(key1, key2)
