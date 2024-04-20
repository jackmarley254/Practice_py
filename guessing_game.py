#!/usr/bin/python3

print("I'm thinking of a number between 1 and 99")

# Ask the user to guess
# Check to see if the guess is <, >, or = secret number
# Print the right message
import random

# Part 1: High or Low

# Assign a secret number
secret_number = random.randint(1, 100)  # Generating a random number between 1 and 100
print("Welcome to the High or Low game!")

while True:
    # Prompt the user to enter a number
    guess = input("Guess the secret number (between 1 and 100): ")

    # Check if the input is a valid number
    if not guess.isdecimal():
        print("Please enter a valid number.")
        continue

    # Convert the input to an integer
    guess = int(guess)

    # Check the user's guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the secret number:", secret_number)
        break

# Part 2: Loop and Random Secret Number

# Reset the secret number
secret_number = random.randint(1, 100)

print("\nNow let's play the game with a new secret number!")

while True:
    guess = input("Guess the secret number (between 1 and 100): ")

    if not guess.isdecimal():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the secret number:", secret_number)
        break
