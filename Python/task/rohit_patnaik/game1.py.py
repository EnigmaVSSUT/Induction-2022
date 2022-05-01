import random

player1 = input("Enter name of first player ")
player2 = input("Enter name of second player ")
target = int(input("Enter the target number: "))
score1 = 0
score2 = 0
while True:
        if (score1 < target) and (score2 < target):
            input(f"{player1} Press Enter to Roll Dice.")
            dice1 = int(random.randint(1, 6))
            print(f"Dice rolled {dice1}")
            score1 = score1+dice1
            input(f"{player2} Press Enter to Roll Dice.")
            dice2 = int(random.randint(1, 6))
            print(f"Dice rolled {dice2}")
            score2 = score2+dice2
            print(f"{player1}'s Score is: {score1}\n{player2}'s Score is: {score2}")
        if score1 > target:
            score1 = score1-dice1
        if score2 > target:
            score2 = score2-dice2
        if score2 == target:
            print(f"Congratulations! {player2} you won")
            break
        if score1 == target:
            print(f"Congratulations! {player1} you won")
            break
