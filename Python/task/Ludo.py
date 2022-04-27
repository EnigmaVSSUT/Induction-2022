import random
import time

print("Welcome to LUDO \n")
time.sleep(1)
print("Rules and Regulations\n-Press enter to roll the dice, when displayed your turn\n-Don't quit game before the end\n\n-Be patient, Best of Luck\n")
time.sleep(2)
player1 = input("Name of Player 1 : ")
player2 = input("Name of Player 2 : ")

Limit = int(input("Enter Target Score : "))
print("High Score : " + str(Limit))
time.sleep(2)
a = 0
b = 0
while True:
    input("Player1")
    dice1 = random.randint(1,6)
    a+=dice1
    print(player1 + "'s Dice gave " + str(dice1))
    if a == Limit:
        print(player1 + " Wins")
        print("Better Luck Next Time " + player2)
        break
    elif a > Limit:
        a -= dice1
    print(player1 + "'s total score " + str(a) )
    input("Player2")
    dice2 = random.randint(1,6)
    b+=dice2
    print(player2 + "'s Dice gave " + str(dice2))
    if b == Limit:
        print(player2 + " Wins")
        print("Better Luck Next Time " + player1)
        break
    elif b > Limit:
        b -= dice2
    print(player2 + "'s total score " + str(b) )
time.sleep(2)
print("Hope you enjoyed")
print("Thank you for Playing LUDO")
time.sleep(5)