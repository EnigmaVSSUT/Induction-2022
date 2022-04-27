import random

while True:
    print("Player 1")
    p1 = input("Enter your name : ")
    print("Player 2")
    p2 = input("Enter your name : ")
    t = int(input("Enter the target number: "))
    scr1 = 0
    scr2 = 0
    while True:
        if (scr1 < t) and (scr2 < t):
            input(f"{p1} press Enter to roll the dice.")
            dice1 = int(random.randint(1, 6))
            print(f"Dice rolled {dice1}")
            scr1 += dice1
            input(f"{p2} press enter to roll the dice.")
            dice2 = int(random.randint(1, 6))
            print(f"Dice rolled {dice2}")
            scr2 += dice2
        if scr1 > t:
            scr1 -= dice1
        if scr2 > t:
            scr2 -= dice2
        print(f"{p1}'s Score: {scr1}\n{p2}'s Score: {scr2}")
        if scr2 == t:
            print(f"{p2} you won the game!!")
            break
        if scr1 == t:
            print(f"{p1} you won the game!!")
            break
    replay = input("Press Y to play again or press any other key to exit : ")
    if replay.lower() == "y":
        continue
    else:
        print("Thank you for playing!!")
        break
