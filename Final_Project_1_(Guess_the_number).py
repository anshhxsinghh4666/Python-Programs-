# GUESS THE NUMBER : 
                    # WAP to generate a random number between 1 and 100 and ask the user to guess the number.
                    # The user should have a maximum of 7 attempts to guess the number.
                    # After each guess, the program should display if the guess is too high or too low.
                    # If the user guesses the number correctly, display a congratulatory message and exit the program.
                    # If the user runs out of attempts, display a message indicating they failed and exit the program.

# random Module : This module provides functions for generating random numbers or characters.

import random

target = random.randint(1, 100) # Generate a random number between 1 and 100

attempts = 0
while True:
    if attempts > 7:
        print("You ran out of attempts. You failed to guess the number.")
        break
    user_choice = (input("Enter your guess number or Quit(Q): "))
    if user_choice == 'q' or user_choice == 'Q':
        break
    user_choice = int(user_choice)
    if user_choice == target:
        print("Success! You guessed the number correctly.")
        break
    elif user_choice > target:
        print("Too high! Try again.")
    elif user_choice < target:
        print("Too low! Try again.")
    elif user_choice < 1 or user_choice > 100:
        print("Invalid input! Please enter a number between 1 and 100.")
    attempts += 1

print("--------Game Over--------")
