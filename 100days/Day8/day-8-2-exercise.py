#Write your code below this line 👇
import math

def prime_checker(number):
    i = 2
    sqr_rt = math.sqrt(number)
    while i < sqr_rt:

        test_prime = number % i
        if test_prime == 0:
            print("It's not a prime number")
            break
#        print(f"{number} modulo ---- {i} = {number % i}")
        i+=1
    if test_prime != 0:
        print("It's a prime number.")
#    for i in range(2, int(math.sqrt(number)) + 1):



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)




