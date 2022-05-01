 ## enigma gaming zone##
print( """********************** welcome to enigma Ludo master ********************** """)
import random
import os

while True:
    name1 = input("Player 1 enter your name : ")
    name2 = input("Player 2 enter your name : ")
    goal = int(input("Enter the goal number: "))
    p1score = 0
    p2score = 0
    
    while True:
        if (p1score < goal) and (p2score < goal):
            input(f"{name1} press Enter to roll the dice.")
            D1 = int(random.randint(1, 6))
            print(f"Dice rolled {D1}")
            p1score = p1score+D1
            input(f"{name2} press enter to roll the dice.")
            D2 = int(random.randint(1, 6))
            print(f"Dice rolled {D2}")
            p2score= p2score+D2
            print(f"{name1}'s Score: {p1score}\n{name2}'s Score: {p2score}") 

        if p1score > goal:
            p1score = p1score-D1

        if p2score > goal:
          p2score= p2score-D2

        if p2score == goal:
            print(f"{name2}  won the game!!")
            break

        if p1score == goal:
            print(f"{name1} won the game!!")
            break

    new1 = input("Press Y to play again or press any other key to exit ==> ")

    if new1.lower() == "y":
        continue
    else:
        print("Thank you for playing!!")
        break
    

