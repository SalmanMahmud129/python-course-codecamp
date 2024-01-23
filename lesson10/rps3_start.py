# all we did is add a while loop so that the game doesnt end until play again is false
import random
from enum import Enum 
import sys

def play_rps():
        
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3



    print("")

    playerchoice = int(input("Enter... \n1 for rock, \n2 for paper, or \n3 for scissors\n"))

    if playerchoice not in [1, 2, 3]:
        print("You must enter 1, 2, or 3")
        return play_rps()# start the game over if they didnt enter a proper choice
        

    computerchoice = int(random.choice("123"))
    print("You chose", str(RPS(playerchoice)).replace('RPS.', ''), ".")
    print("Python chose", str(RPS(computerchoice)).replace('RPS.', ''), ".")
    print("")

    if playerchoice == 1 and computerchoice == 3:
        print("👌You win!")
    elif playerchoice == 2 and computerchoice == 1:
        print("👌You win!")
    elif playerchoice == 3 and computerchoice == 2:
        print("👌You win!")
    elif playerchoice == computerchoice:
        print("👀Tie game")
    else:
        print("🐍Python wins!")
    
    print("\nPlay again?")
    while True:

        playagain = input("\nY for yes or Q to quite\n")
        if playagain.lower() not in ["y", "q"]:
            print("Please enter a valid choice")
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps() # start the game over with a recursive call
    else:
        print("\n🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")
        # or you can use a break


play_rps()