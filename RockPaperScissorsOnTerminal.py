from random import randint

def main() :
    print('Hello World! Those are some games i made to study python!')
    rockPaperScissors()

def rockPaperScissors() :
    strings = [{'Game #1 - Rock, Paper, Scissors!'}]
    inputs = ['rock', 'paper', 'scissors']
    validInput = 0

    print('Game #1 - Rock, Paper, Scissors!')
    
    while True: #while the input is invalid, wait for a valid input
        print('Pick a number from 1 to 3 or write your selection.')
        playerHand = input().lower()

        if (playerHand.isnumeric()) :#check if input is a number and a valid number
            playerHand = int(playerHand) 
            if(playerHand > 0 and playerHand < 4) :
                break
            else:
                print('Not a valid number (1-3)')

        else :
            for idx,i in enumerate(inputs) : #check if the input is a string, if yes, convert to int
                if(str(playerHand) == str(i)) :
                    playerHand = int(idx) + 1
                    validInput = 1
                    break

            if (validInput == 1): break #break while loop since the input is valid
    
    computerHand = int(randint(1,3)) #draw a 'hand' for the computer
    playerHand = int(playerHand) #idk why but i need to use this to make sure it's and integer

    print('you chose:',inputs[playerHand-1],' and the computer chose:',inputs[computerHand-1]) #preview results

    if(int(playerHand) == int(computerHand)) :
        print('Draw!') 
        return

    if(playerHand == 1) :#default stuff from rock,paper,scissors game, and return to main func
        if(computerHand == 2) :
            print('Computer wins!')
        else:
            print('You wins!')
        return
    if(playerHand == 2) :
        if(computerHand == 3) :
            print('Computer wins!')
        else:
            print('You wins!')
        return
    if(playerHand == 3) :
        if(computerHand == 1) :
            print('Computer wins!')
        else:
            print('You wins!')
    else:
        print('wtf')
    return


if __name__ == '__main__': main() #execute main only if this is executed as a script and not imported as a module