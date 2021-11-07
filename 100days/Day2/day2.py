##Data Types
#
##String
#
#print("Hello"[4])
#
#
#print("123" + "345")
#
##Integer
#
#print(123 + 345)
#
##Python interpreter removes "_" from an int. For example an int 123_456_789  can be written with "_"
##for readability, but interpreter will remove "_" and the int will be 123456789
#
#
#
##Float
#
#print(3.145)


#num_char = len(input("What is your name? ")) #integer
#
#new_num_char = str(num_char) 
##print("your name has " + num_char + " characters")
#
#print("your name has " + new_num_char + " characters") #<<<---- this is type conversion (type casting)
#print(type(num_char))
#
#print(type(new_num_char))

#a = 123
#print(type(a))
#a = float(123)

#print(type(a))
#print(70 + float("100.54"))

###Asssignment 2.1
# write a program that adds the digits in a 2 digit number. (if the input was 35, you should output 3 + 8 = 8

#two_dig = (input("Enter a two digit number: \n")) #take string input
#
#
#a = int(two_dig[0]) + int(two_dig[1]) #convert str to int and add them together
#print(type(two_dig))
#print(a)

#DAY-2-END

#print(3 * (3 + 3) / 3 - 3)
#
#score = 0
#height = 1.8
#isWinning = True
#f-String
#print(f"Your score is {score}, your height is {height}, youre winning{isWinning}" )

#print("Your score is {}, your height is {}, youre winning{}".format(score, height, isWinning))


#day-2-3-3exercise calculate the number of days weeks and months you have left if you were to live to 90
# https://waitbutwhy.com/2014/05/life-weeks.html
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
age_90 = 90 
current_age = int(age)
#Write your code below this line 👇
days = age_90 * 365 - current_age * 365  
weeks = age_90 * 52 - current_age * 52
months = age_90 * 12 - current_age * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")



