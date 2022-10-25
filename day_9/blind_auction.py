import art
import os
valid = True
print(art.logo)
print("Welcome to the secret auction program.")
dict = {}
def highest_bidder(dict):
    highest = 0
    highest_b = ''
    for key in dict:
        if highest < dict[key]:
            highest_b = key
            highest = dict[key]
    print(f"{highest_b} is the winner with a bid of ${highest}! Congratulations!")
while valid:
    name = input("What is your name?: ") # key
    bid = int(input("What's your bid?: $")) # value
    dict[name] = bid
    user = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if user == 'no':
        highest_bidder(dict)
        valid = False
    elif user == 'yes':
        os.system('cls||clear')
        valid = True
    else:
        valid = False
        print("Invalid Input")
    