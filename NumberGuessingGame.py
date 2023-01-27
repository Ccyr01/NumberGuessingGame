"""
Christian C. 1/27/2023
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # Display intro message
    count = 1;
    print("Welcome to the Number Guessing Game!!")
    numberToGuess = random.randint(0,10)
    #Checking if user entered value is valid
    try:
        userGuess = int(input("Pick a number between 0 and 10 inclusive.\n"))  
    #Non int entered or invalid one
    except ValueError:
        print("Please enter a valid value")
    #Have a valid number at this point.
    #Proceed with game
    else:      
        while userGuess != numberToGuess:
            if userGuess < numberToGuess:
                print("To low")
                count+=1
            else:
                print("To high")
                count+=1
            userGuess = int(input("pick a number."))  

        if count < 2:
            print("Wow!! Can't believe you guessed it in {}".format(count)+ " try. You've got good luck")
        elif count <= 3:
            print("Nice. Guessed it in {}".format(count) + " tries. That's good luck.")
        else:
            print("Got it! It took about {}".format(count)+" times.")
    #farewell
    print("Give it another shot if you want to test your luck!")


# Kick off the program by calling the start_game function.
start_game()