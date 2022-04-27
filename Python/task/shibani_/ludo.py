
import random
goal = int(input("Enter the goal :\n"))
player1_score = 0
player2_score = 0

while (player1_score < goal) and (player2_score < goal) :
    print("player1 press enter to roll the dice :\n ")
    dice_1 = int(random.randint(1,6))
    player1_score = player1_score + dice_1
    print(player1_score)

    print("player2 press enter to roll the dice :\n")
    dice_2 = int(random.randint(1,6))
    player2_score = player2_score + dice_2
    print(player2_score)

    if player1_score > goal :
        player1_score = player1_score - dice_1
    if player1_score == goal :
        print("Congo! player1 won the game")
        break


    if player2_score > goal :
        player2_score = player2_score - dice_2
    if player2_score == goal :
        print("Congo! player2 won the game")
        break


