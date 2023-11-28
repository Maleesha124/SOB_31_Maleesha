import random

def compare_numbers(number, user_guess):
    ## your code here
    cows = 0 #counting cows
    bulls = 0 #counting bulls

    for i in range(len(number)): #for the random 4 digit number generated
        if user_guess[i] == number[i]: #if the user guesses the number correctly, 1 bull is added
            bulls+=1
        elif user_guess[i] in number: #if the user guesses the number incorrectly, 1 cow is added
            cows+=1
            
    return cows, bulls #changed the return to fit the code

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
#removed this line as it removes the purpose of the game

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")#corrected 'raw_input' to 'input'
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "guesses! The number was "+str(number))#added the word guesses
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
