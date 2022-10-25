import art
import math

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
    } 
print(art.logo)
def calculator():
    valid = True
    num1 = float(input("What's the first number?: "))
    while valid:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        for symbol in operations:
            print(symbol)
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user = input("Type 'y' to contuneu calculating with 16, or type 'n' to start a new calculation: ").lower()
        if user == 'n':
            calculator()
        elif user == 'y':
            num1 = answer
        else:
            print("Invalid Input, the application will exit.")
            valid = False

calculator()