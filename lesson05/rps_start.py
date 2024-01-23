# value = input('Please enter a value: \n')

# print(value)
import random
from enum import Enum 
import sys

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(2)) # -> RPS.PAPER
# print(RPS.ROCK) # -> RPS.RCOK
# print(RPS['ROCK']) # -> RPS.ROCK
# print(RPS.ROCK.value) # -> 1
# sys.exit()


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