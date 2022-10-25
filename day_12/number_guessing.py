import random
def main():
    logo = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ |
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/ """
    print(logo)
    target = random.randint(1, 101)
    attempts = 0
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty, type 'easy' or 'hard': ")
    if difficulty.lower() == 'easy':
        attempts = 10
    elif difficulty.lower() == 'hard':
        attempts = 5
    num = 0
    valid = True
    while valid:
        print(f"You have {attempts} attempts remaining to guess the number.")
        num = int(input("Make a guess: "))
        
        if num > target:
            print("Too high.")
            print("Guess again.")
        elif num < target:
            print("Too Low.")
            print("Guess Again.")
        else:
            print(f"You got it! The answer was {target}")
            break
        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses, you lose. The number was {target}")
            valid = False


main()