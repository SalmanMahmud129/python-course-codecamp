# all we did is add a while loop so that the game doesnt end until play again is false
import random
from enum import Enum 
import sys

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    
playagain = True

while playagain:


    print("")

    playerchoice = int(input("Enter... \n1 for rock, \n2 for paper, or \n3 for scissors\n"))

    if playerchoice < 1 or playerchoice > 3:
        print("You must enter 1, 2, or 3")

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

    playagain = input("\nDo you want to play again\nY for yes or Q to quite\n\n")
    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False
        # or you can use a break
sys.exit("Bye! 👋")