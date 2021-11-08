#import random
#import day4_mod
#
#print(random.randint(100, 200))
##print(day4_mod.pi)
##random.uniform generates floats in range
##random_float = random.uniform(0, 5)
##or we can use random.random to generate floats. random.random generates floats between 0 and 1 exclusively
##however to expand the range we can just multiply it by 5.
#random_float = random.random() * 5 
#print(random_float)
#
#
#love_score = random.randint(1, 100)
#print(love_score)


#*****LISTS****
states_of_america = ["Delaware", "Pennsylvania"]


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
#my_str = "MOJA RIJEC"
#print(my_str[1])
#APPEND
states_of_america.append("Puerto Rico")
print(states_of_america)
#EXTEND
states_of_america.extend(["zoriville", "kubana"])

print(states_of_america)
