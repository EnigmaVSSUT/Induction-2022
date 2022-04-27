import random
while True:
    NAME1 = input("ENTER NAME'S OF PLAYER1:=> ")
    NAME2 = input("ENTER NAME'S OF PLAYER2:=> ")
    GOAL= int(input("DECIDE THE TARGET:=> "))
    TOTAL_player1 = 0
    TOTAL_player2 = 0
    while True:
        if (TOTAL_player1 < GOAL) and (TOTAL_player2 < GOAL):
            input(f"{NAME1} press Enter to roll the dice.")
            dice1 = int(random.randint(1, 6))
            print(f"Dice rolled {dice1}")
            TOTAL_player1 = TOTAL_player1+dice1
            input(f"{NAME2} press enter to roll the dice.")
            dice2 = int(random.randint(1, 6))
            print(f"Dice rolled {dice2}")
            TOTAL_player2 = TOTAL_player2+dice2
            print(f"{NAME1}'s Score: {TOTAL_player1}\n{NAME2}'s Score: {TOTAL_player2}")

        if  TOTAL_player1 > GOAL:
            TOTAL_player1 = TOTAL_player1-dice1

        if TOTAL_player2 > GOAL:
            TOTAL_player2 = TOTAL_player2-dice2

        if TOTAL_player2 == GOAL:
            print(f"##### {NAME2} you won the game #####")
            break

        if TOTAL_player1 == GOAL:
            print(f"###### {NAME1} you won the game #####")
            break

    VICTORY = input("##### ENTER j TO PLAY AGIAN OR ENTER ANY KEY TO EXIT ######")

    if VICTORY.lower()=="j":
        continue
    else:
        print("*************")
        print("Thank you for playing!!")
        break