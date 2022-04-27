import random
import time

print("Welcome to LUDO Lite\n")
time.sleep(2)
print("Rules and Regulations\n*Press enter to roll the dice, when displayed your turn\n*Don't cheat by editing this code before a new game\n\n*Be patient, Trust on Luck\n")
time.sleep(5)
player1 = input("Name of Player 1 : ")
player2 = input("Name of Player 2 : ")
maxLimit = int(input("Enter Target Score : "))
print("High Score : " + str(maxLimit))
time.sleep(2)
a = 0
b = 0
while True:
    input("Player1")
    dice1 = random.randint(1,6)
    a+=dice1
    print(player1 + "'s Dice gave " + str(dice1))
    if a == maxLimit:
        print(player1 + " Wins")
        break
    elif a > maxLimit:
        a -= dice1
    print(player1 + "'s total score " + str(a) )
    input("Player2")
    dice2 = random.randint(1,6)
    b+=dice2
    print(player2 + "'s Dice gave " + str(dice2))
    if b == maxLimit:
        print(player2 + " Wins")
        break
    elif b > maxLimit:
        b -= dice2
    print(player2 + "'s total score " + str(b) )
time.sleep(2)
print("Hope it worked successfully")
print("Thank you for Playing LUDO Lite")
time.sleep(3)
print("For any modifications needed or suggested, kindly share with us through mail\ncoder.jp333@gmail.com\nThanks again")
time.sleep(10)