#calculate BMI in python
#    https://en.wikipedia.org/wiki/Body_mass_index
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

print("Your BMI is: " + str(round((float(weight) / float(height) ** 2),None)) + "\n")
#instead if we type casted the resule to an int this would just chop off everything after the decimal point)


#  // === floor division forces result into an INT. 



