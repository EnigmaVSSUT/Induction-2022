import random

player1 = 0
player2 = 0
goal = int(input("Enter the goal:\n"))

while (player1 < goal) and (player2 < goal):
    input("Player 1 - Hit Enter to roll Dice!")
    d1 = int(random.randint(1, 6))
    player1 = player1 + d1
    print(d1)
    if player1 > goal:
        player1 = player1 - d1
    if player1 == goal:
        print("Player 1 Wins the Game!")
        break

    input("Player 2 - Hit Enter to roll Dice!")
    d2 = int(random.randint(1, 6))
    player2 = player2 + d2
    print(d2)
    if player2 > goal:
        player2 = player2 - d2
    if player2 == goal:
        print("Player 2 Wins the Game!")
        break

    print("Player 1 Score: ", player1)
    print("Player 2 Score: ", player2)
