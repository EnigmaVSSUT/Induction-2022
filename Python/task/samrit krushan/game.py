import random

player1 = 0
player2 = 0
goals= int(input("Enter the goal to be :\n"))

while (player1 < goals) and (player2 < goals):
    input("Player 1 - press enter to roll the Dice!")
    a = int(random.randint(1, 6))
    player1 = player1 + a
    print(a)
    if player1 > goals:
        player1 = player1 - a
    if player1 == goals:
        print("Player 1 Won the Game!")
        break

    input("Player 2 - press enter to roll the Dice!")
    b = int(random.randint(1, 6))
    player2 = player2 + b
    print(b)
    if player2 > goals:
        player2 = player2 - b
    if player2 == goals:
        print("Player 2 Won the Game!")
        break

    print("Player 1 Score is: ", player1)
    print("Player 2 Score is: ", player2)