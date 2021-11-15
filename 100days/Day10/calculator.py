import random
from art import logo
def add(n1, n2):

    return n1 + n2

def subtract(n1, n2):

    return n1 - n2

def multiply(n1, n2):

    return n1 * n2


def divide(n1, n2):

    return n1 / n2

operations = {
        "+": add, 
        "-": subtract, 
        "*": multiply, 
        "/": divide
        ,
        }


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    
    
    for symbol in operations:
        print(symbol)
    should_continue = True 
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        #if operation_symbol == "+":
        #    answer = add(num1, num2)
        #
        #elif operation_symbol == "-":
        #    answer = subtract(num1, num2)
        #
        #elif operation_symbol == "*":
        #    answer = multiply(num1, num2)
        #
        #elif operation_symbol == "/":
        #    answer = divide(num1, num2)
        
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or tye 'n' to exit.: ") == "y":
            num1 = answer
        else:
            should_continue = False 
            calculator()
calculator()
   
#    operation_symbol = input("Pick an operation: ")
#    num3 = int(input("What's the next number?: "))
#    calculation_function = operations[operation_symbol]
#    #second_answer = calculation_function(calculation_function(num1, num2), num3)
#    second_answer = calculation_function(first_answer, num3)
#    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}") 
