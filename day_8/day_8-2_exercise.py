#Write your code below this line 👇
def prime_checker(number):
    if number == 1:
        print("It's not a prime number.")
    elif(number != 2 and number % 2 == 0) or (number != 3 and number % 3 == 0) or (number != 5 and number % 5 == 0) or (number != 7 and number % 7 == 0) or (number % 9 == 0 and number != 9):
        print("It's not a prime number.")
    else:
        print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)