#Library Inclusion
import random
import time

#Head
time.sleep(1)
print()
print("Welcome to LUDO Game\n")
time.sleep(1)
print("Press 'Enter' each time you want to roll the dice\n")
time.sleep(1)

#Inputs (Player Names and Target Score)
p1 = input("Player One Name : ")
time.sleep(1)
p2 = input("Player Two Name : ")
time.sleep(1)
target = int(input("Target Score : "))

#Loop Initiation for Play Again
while True:
    score1 = 0
    score2 = 0

    #Loop Initiation for Repeated Dice Rolls until Target score is Achieved
    while True:

        #Player One Dice Roll
        input(p1 + " Press Enter")
        rollOne = random.randint(1,6)
        print(p1 + " rolled " + str(rollOne))

        #Player One Total Score after each Dice Roll
        score1+=rollOne

        #Condition Check for Score Saturation
        if score1 == target:
            print(p1 + " Victory")
            print(p2 + " Better Luck Next Time")
            break
        elif score1 > target:
            score1-=rollOne

        #Print Score
        print(p1 + " Score " + str(score1) + "\n")


        #Player Two Dice Roll
        input(p2 + " Press Enter")
        rollTwo = random.randint(1,6)
        print(p2 + " rolled " + str(rollTwo))

        #Player Two Total Score after each Dice Roll
        score2+=rollTwo

        #Condition Check for Score Saturation
        if score2 == target:
            print(p2 + " Victory")
            print(p2 + " Better Luck Next Time")
        elif score2 > target:
            score2-=rollTwo

        #Print Score
        print(p2 + " Score " + str(score2))

    #Play Again Option
    time.sleep(2)
    print("Wanna Play Again?")
    again = input("Choose 1 for Once More\no to Exit")
    time.sleep(1)
    if again == '1':
        continue
    elif again == '0':
            break
    else:
        print("Pagla gaye ho ka?\n")
        break

#Conclusion Statement
print("Thank you for Playing Ludo Game\n")
print("Coded by Homo sapiens")
time.sleep(1)
print("From Earth")
time.sleep(5)