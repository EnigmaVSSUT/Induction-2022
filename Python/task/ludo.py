import random

while True:
    player1 = input("enter player_1 name :- ")
    player2 = input("enter player_2 name :- ")
    target = int(input("Enter the target :- "))
    scr1 = 0
    scr2 = 0
    while True:
        if (scr1 < target) and (scr2 < target):
            input(f"{player1} press Enter to roll the dice.")
            dice1 = int(random.randint(1, 6))
            print(f"Dice rolled {dice1}")
            scr1 = scr1+dice1
            input(f"{player2} press enter to roll the dice.")
            dice2 = int(random.randint(1, 6))
            print(f"Dice rolled {dice2}")
            scr2 = scr2+dice2
            print(f"{player1}'s Score: {scr1}\n{player2}'s Score: {scr2}")

        if scr1 > target:
            scr1 = scr1-dice1

        if scr2 > target:
            scr2 = scr2-dice2

        if scr2 == target:
            print(f"{player2} you won the game!!")
            break

        if scr1 == target:
            print(f"{player1} you won the game!!")
            break

    replay = input("Press Y to play again or press any other key to exit ==> ")

    if replay.lower() == "y":
        continue
    else:
        print("Thank you for playing..")
        break