import random

while True:
    p1 = input("Player 1 Enter 1st player name")
    p2 = input("Player 2 Enter 2nd player name")
    target = int(input("Enter the target number: "))
    score1 = 0
    score2 = 0
    while True:
        if (score1 < target) and (score2 < target):
            input(f"{p1} Press ENTER to roll the dice.")
            dice1 = int(random.randint(1, 6))
            print(f"Dice rolled {dice1}")
            score1 = score1 + dice1
            input(f"{p2} Press ENTER to roll the dice.")
            dice2 = int(random.randint(1, 6))
            print(f"Dice rolled {dice2}")
            score2 = score2 + dice2
            print(f"{p1}'s score is: {score1} \n {p2}'s score is: {score2}")
        if score1 > target:
            score1 -= dice1

        if score2 > target:
            score2 -= dice2
        print(f"{p1}'s Score: {score1}\n{p2}'s Score: {score2}")

        if score1 == target:
            print(f"{p1} Cong Rats,you won the game. ")
            break
        if score2 == target:
            print(f"{p2} Cong Rats,You won the game. ")
            break
       
    replay = input("Press y to play again or press any other key to exit : ")
    if replay.lower() == "y":
        continue
    else:
        print("Thank you for playing!!")
        break