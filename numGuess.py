# User guess a secret number from a number range:
import random

def userGuess(x):
    random_number = random.randint(1, x)
    print(random_number)
    guess = 0
    tries = 1

    while guess != random_number:
        guess = int(input(f"guess a number between 1 to {x}: "))
        if guess < random_number:
            print("too low! guess again")
            tries += 1
        elif guess > random_number:
            print("too high! guess again")
            tries += 1
    print(f"You got the number. your guess number {guess} matches with {random_number} \ you got in {tries} tries.")

# userGuess(10)

# computer guess a secret number from a user input:

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'correct':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        guess = random.randint(low, high)
        feedback = (input(f'is {guess} too high, too low or correct? ')).lower()
        if feedback == 'high':
            high = guess - 1
        elif feedback == 'low':
            low = guess + 1
    print(f"{guess} is the number, you got the number!")

computerGuess(5)