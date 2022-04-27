import random
from random import randint
import time

P1 = input("1st player is ")
P2 = input("2nd player is ")


def diceRoll(num_sides=6):
    return random.randint(1, num_sides)


def playGameOfDice(playername):
    a = int(input("Enter the winning score : "))
    # print("Hello,Welcome to game of dice! First to ", a, "points wins!")
    score1 = 0
    score2 = 0
    while score1 != a and score2 != a:
        print("The current score is: ", P1,
              score1, ",", P2, score2)
        input("Press 'Enter' to roll.")
        player1Roll = diceRoll()
        if(score1 + player1Roll <= a):
            score1 = score1 + player1Roll
        else:
            score1 = score1

        print("", P1, "'s dice rolled to.......... "+str(player1Roll)+".")
        time.sleep(2)
        player2Roll = diceRoll()
        if(score2 + player2Roll<= a):
            score2 = score2 + player2Roll
        else:
            score2 = score2
        print("", P2, "'s dice rolled to.......... "+str(player2Roll)+".")
        time.sleep(2)

    if score1 > score2:
        print("Congrats!!", P1, "wins the game")
    elif (score1 == score2):
        print("The game is Tied")
    else:
        print(P2, "wins the game")

    if (score1 > score2):
        return True
    else:
        return False


playerWins = playGameOfDice(P1)
if(playerWins == True):
    print("")
