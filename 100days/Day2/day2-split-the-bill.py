#this program will compute the amount of tip required if we'espliting is


#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill = float(input("Weclcome to tip calculator\nWhat was the total bill\n"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?\n")) 
number_of_people = int(input("How many people to split the bill\n"))
payup = round((total_bill * (1 + tip_percent / 100) / number_of_people),2)
'''Below is the format specifier that has format as:
    "{:.2f}" >>> meaning 2 digits after decimal point - similar to C
'''   
print( "Each person should pay " + "{:.2f}".format(payup, 2))
