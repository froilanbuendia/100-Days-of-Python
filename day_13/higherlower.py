from operator import truediv
import art
import game_data
import random
import os
def getData():
    num = random.randrange(0, len(game_data.data) - 1)
    person = game_data.data[num]
    return person

def getComparison(userinput, A, B):
    if userinput == 'A':
        if A.get('name') >= B.get('name'):
            return True
        else:
            return False
    elif userinput == 'B':
        if B.get('name') >= A.get('name'):
            return True
        else:
            return False


def main():
    valid = True
    score = 0
    print(art.logo)
    while valid:
        A = getData()
        print(f"Compare A: {A.get('name')}, a {A.get('description')}, from {A.get('country')}")
        print(art.vs)
        B = getData()
        print(f"Against B: {B.get('name')}, a {B.get('description')}, from {B.get('country')}")
        user = input("Who has more followers? Type 'A' or 'B': ")
        comparison = getComparison(user, A, B)
        os.system('cls||clear')
        print(art.logo)
        if comparison == False:
            valid = False
            print(f"Sorry, that's wrong. Final score: {score}")
        else:
            score += 1
            print(f"You're right! Current score: {score}")
    
main()