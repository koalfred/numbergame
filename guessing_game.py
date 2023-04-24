#"""
#Project 1 - Number Guessing Game
#--------------------------------
#
#For this first project you can use Workspaces. 
#
#NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.
#
#"""

import random
from statistics import mean, median, mode

attempts = []

def start_game():
#    """Psuedo-code Hints
#    
#    When the program starts, we want to:
#    ------------------------------------
#    1. Display an intro/welcome message to the player.
#    2. Store a random number as the answer/solution.
#    3. Continuously prompt the player for a guess.
#      a. If the guess greater than the solution, display to the player "It's lower".
#      b. If the guess is less than the solution, display to the player "It's higher".
#    
#    4. Once the guess is correct, stop looping, inform the user they "Got it"
#         and show how many attempts it took them to get the correct number.
#    5. Save their attempt number to a list.
#    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
#    7. Ask the player if they want to play again.
#    
#    ( You can add more features/enhancements if you'd like to. )
#    """
    # write your code inside this function.
    print("Welcome to the Number Guessing Game!")
    if attempts:
        print(f'Your current best score is {min(attempts)} attempts.')
    attempt_count = 1
    num = input("I am thinking of a number between 1 and 100. What number am I thinking of? ")
    secret_num = random.randint(1, 100)
        
    while num != secret_num:
        attempt_count += 1
        try:
            if int(num) >= 1 and int(num) <= 100:
                if int(num) > secret_num:
                    num = int(input("It's lower. "))
                elif int(num) < secret_num:
                    num = int(input("It's higher. "))
            else:
                num = int(input("The number must be between 1 and 100. "))
        except ValueError:
            num = input("This is not a valid number. ")

    attempts.append(attempt_count)
    print(attempts)
    print(f'Got it! It took {attempt_count} attempts to guess the number.')
    print(f'Mean attempt: {mean(attempts)}') 
    print(f'Median attempt: {median(attempts)}')
    print(f'Modal attempt: {mode(attempts)}')
    
    yes_or_no = input("Do you want to play again? Y/N ")
    
    if yes_or_no.lower() == "y":
        start_game()
    elif yes_or_no.lower() == "n":
        print("No worries, have a good day!")
# Kick off the program by calling the start_game function.
start_game()