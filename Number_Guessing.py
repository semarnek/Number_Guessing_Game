import random
import math

def guess(num, live):
    make_guess = 0
    while make_guess != num and live > 0:
        print(f"You have {live} attempts remaining to guess the number.")
        make_guess = int(input("Make a guess: "))
        if make_guess == num:
            return make_guess
        elif abs(make_guess - num) <= 5:
            print("Too close.")
        elif abs(make_guess - num) <= 10:
            print("A little close.")
        else:
            print("You were far from the number.")

        live -= 1
        if live == 0:
            return 0
        if make_guess > num:
            print("Guess lower. Guess again.")
        else:
            print("Guess higher. Guess again.")

    return 0


number = random.randrange(1,101)
lives = 0
success = 0

print("Welcome to the Number Guessing Game!")

print("I am thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")

if difficulty == "easy":
    lives = 10

elif difficulty == "hard":
    lives = 5


success = guess(number, lives)

if success != 0:
    print(f"You got it! The answer was {number}.")
else:
    print(f"You've run out of guesses, you lose. The number was {number}")
