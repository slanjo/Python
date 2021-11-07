#calculate BMI in python
#    https://en.wikipedia.org/wiki/Body_mass_index
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
#day 2 BMI
#print("Your BMI is: " + str(round((float(weight) / float(height) ** 2),None)) + "\n")
#instead if we type casted the resule to an int this would just chop off everything after the decimal point)

bmi = round(((float(weight) / float(height) ** 2)), None)
obesity = " "

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweigth\n") 
elif bmi < 25: 
    print(f"Your BMI is {bmi}, you have a normal weigth\n") 
elif bmi < 30: 
    print(f"Your BMI is {bmi}, you are slightly overweight\n") 
elif bmi < 35: 
    print(f"Your BMI is {bmi}, you are obese\n") 
else:
    print(f"You are clinically obese")
print(f"Your BMI is: {bmi}\n")


#  // === floor division forces result into an INT. 



