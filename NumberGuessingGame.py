"""
Christian C. 1/27/2023
TeamTreeHouse
Going for exceeds expectations
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game(count, numberToGuess, highScore):
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
    
    #Checking if user entered value is valid
    print("high score = {}".format(highScore))
    try:
        userGuess = int(input("Pick a number between 0 and 10 inclusive.\n")) 
        #Checking if in range if not ask for input again 
        if userGuess < 0 or userGuess > 10:
            print("Number is out of range try again")
            userGuess = int(input("Pick a number between 0 and 10 inclusive.\n"))  

        #Have a valid number at this point.
        #Proceed with game
        while userGuess != numberToGuess:
            if userGuess < numberToGuess:
                print("To low")
                count+=1
            else:
                print("To high")
                count+=1
            userGuess = int(input("pick a number.\n"))  

        #Congragulate
        if count < 2:
            print("Wow!! Can't believe you guessed it in {}".format(count)+ " try. You've got good luck")
        elif count <= 3:
            print("Nice. Guessed it in {}".format(count) + " tries. That's good luck.")
        else:
            print("Got it! It took about {}".format(count)+" times.")
        
        #Check if high score was beat
        if count < highScore:
            highScore = count
            print("New high score...{}".format(highScore))

        #farewell
        #Or Not
        #Get user input y or Y and run the game again
        print('''Give it another shot if you want to test your luck!
Continue? ''')
        answer = (input("Type y for yes or n to exit.\n"))
        if answer.lower() == "y":
            start_game(1, random.randint(0,10),highScore)
        else:
            exit()
            
    #Non int entered or invalid one
    except ValueError:
        print("Please enter a valid value")
        start_game(count, numberToGuess,highScore)
 
# Kick off the program by calling the start_game function.
print("Welcome to the Number Guessing Game!!")
count = 1
numberToGuess = random.randint(0,10)
highScore = 10;

start_game(count, numberToGuess, highScore)