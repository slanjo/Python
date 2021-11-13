
programming_dictionary = {

        "Bug": "An error in a program that prevents the program from running as expected.", 
        "Function": "A piece of code that you can easily call over and over again.",
        }
print(programming_dictionary)

programming_dictionary["Loo"] =  "the action of doing something over and over"

print(programming_dictionary)

#create a dictionary
empty_dictionary = {}

#(Also)Wipe an existing dictionary
#programming_dictionary = {}

#Edit an item in a dict
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)
#Loop through dictionary
for key in programming_dictionary:
    print( programming_dictionary[key])
