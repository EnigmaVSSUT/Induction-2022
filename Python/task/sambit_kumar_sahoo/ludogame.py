import random
from random import randint
import time

player1Name = input("Please enter player1 name:")
player2Name = input("Please enter player2 name:")


def diceRoll(num_sides=6):

    return random.randint(1, num_sides)


def playGameOfDice(player1Name):
    t = int(input("Enter a score to reach to win the game : "))
    player1Score = 0
    player2Score = 0
    while player1Score != t and player2Score != t:
        print("The current score is: ", player1Name,
              player1Score, player2Name, player2Score)
        input("Press 'Enter' to roll the dice.")
        player1Roll = diceRoll()
        if(player1Score+player1Roll <= t):
            player1Score = player1Score+player1Roll
        else:
            player1Score = player1Score
        print("", player1Name, "got number "+str(player1Roll)+".")
        time.sleep(2)
        player2Roll = diceRoll()
        if(player2Score+player2Roll <= t):
            player2Score = player2Score+player2Roll
        else:
            player2Score = player2Score
        print("", player2Name, "got number "+str(player2Roll)+".")
        time.sleep(2)
    if player1Score > player2Score:
        print("Congrats!", player1Name, "win the game")
    elif (player1Score == player2Score):
        print("It's Tie")
    else:
        print("Congrats!", player2Name, "win the game")

    if (player1Score > player2Score):
        return True
    else:
        return False


playerWins = playGameOfDice(player1Name)
if(playerWins == True):
    print("")
