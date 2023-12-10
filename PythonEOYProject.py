#Number Guessing Game
#Sophie Bauer

import random

    #print function for the opening statements of the game
def PrintOpeningStatements():
    print(f'Welcome to Random Number Generator.')
    print(f'You have 5 tries to guess a number between 1 - 50.')
    print()
    print(f'Now generating a random number...')


    #function that generates a random number to send to the Game() function
def RandomNumber():
    yourRandNum = random.randint(1,51)
    
    return yourRandNum


    #function that acquires an integer number from the user
def GetUserNum():
    try:                                #try except block that makes sure user input is an integer
        guess = int(input())
    except:                             #if user input is not an int, it asks for one and gets user input again
        print()
        print('Please enter a number!')
        print('Enter your guess:')
        guess = int(input())
    
    return guess                        #sends the user guess over to the Game() function


    #print function that checks if the user guess is higher or lower than the random number
def HigherOrLower(userNum, randNum):
    if userNum > randNum:
        print(f'The number is lower than {userNum}.')
    elif userNum < randNum:
        print(f'The number is higher than {userNum}.')


    #main game function that calls 
def Game():
    yourRandNum = RandomNumber()        #calls RandomNumber() function to generate the random number and assigns it locally to variable
    
    for i in range(5):                  #for loop that cycles through 5 times 
        print()
        print(f'Attempt {i + 1}!')
        print('Enter your guess:')
        user_guess = GetUserNum()       #calls GetUserNum() function to receive user input for the "guess" and assigns the input to variable
        
        if user_guess == yourRandNum:           #if-else statement that checks if the user guess is matching the random generated number
            print()
            
            print(f'You found it! {yourRandNum} was the correct number.')
            
            break
        else:
            print()
            
            print(f'Wrong. {user_guess} was not the correct number.')
            HigherOrLower(user_guess,yourRandNum)               #calls HigherOrLower() function to check if the user guess is higher/lower than the random number as a hint
            
            print()
            
            print('Guess again!')
            continue

#-------------------------------------------------------------------------------

PrintOpeningStatements()        #initiates opening statements

Game()                          #initiates game by calling Game() function



    



