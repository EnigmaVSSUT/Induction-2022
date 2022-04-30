import random

while True:
    player1 = input(" enter Player 1's name ==> ")
    player2 = input(" enter Player 2's name ==> ")
    target = int(input("Enter the number targeted: "))
    score1 = 0
    score2 = 0
    while True:
        if (score1 < target) and (score2 < target):
            input(f"{player1} now press Enter to roll the dice.")
            dice1 = int(random.randint(1, 6))
            print(f"Dice rolled {dice1}")
            score1 = score1+dice1
            input(f"{player2} press enter to roll the dice.")
            dice2 = int(random.randint(1, 6))
            print(f"Dice rolled {dice2}")
            score2 = score2+dice2
            print(f"{player1}'s Score: {score1}\n{player2}'s Score: {score2}")

        if score1 > target:
            score1 = score1-dice1

        if score2 > target:
            score2 = score2-dice2

        if score2 == target:
            print(f"{player2} yay! you won the game!!")
            break

        if score1 == target:
            print(f"{player1}yay! you won the game!!")
            break

    replay = input("Press Y to play again or press any other key to exit ==> ")

    if replay.lower() == "y":
        continue
    else:
        print("Thanks for playing!")
        break
