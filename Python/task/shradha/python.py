import random
print ("LUDO")

player1 = 0
player2 = 0
goal = int(input("Enter the total goal:\n"))

while (player1 < goal) and (player2 < goal):
    print("Dice rolled by-Player 1")
    d1 = int(random.randint(1, 6))
    player1 = player1 + d1
    print(d1)
    if player1 > goal:
        player1 = player1 - d1
    if player1 == goal:
        print("Player 1 Wins the Game!")
        break

    input("Dice rolled by-Player 2")
    d2 = int(random.randint(1, 6))
    player2 = player2 + d2
    print(d2)
    if player2 > goal:
        player2 = player2 - d2
    if player2 == goal:
        print("Player 2 Wins the Game!")
        break

    print("Player 1 Scored: ", player1)
    print("Player 2 Scored: ", player2)