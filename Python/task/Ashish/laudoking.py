import random
import time
print("welcome Ak universe")
print("Press enter to roll the dice")
time.sleep(2)
player1 = input("Name of Player 1 : ")
player2 = input("Name of Player 2 : ")
highScore = int(input("Enter Target Score : "))
time.sleep(2)
a = 0
b = 0
while True:
    input("Player1")
    dice1 = random.randint(1,6)
    a=dice1+a
    print(player1 + "'s Dice gave " + str(dice1))
    if a == highScore:
        print(player1 + " Wins")
        break
    elif a > highScore:
        a = a-dice1
    print(player1 + "'s total score " + str(a) )
    input("Player2")
    dice2 = random.randint(1,6)
    b=dice2+b
    print(player2 + "'s Dice gave " + str(dice2))
    if b == highScore:
        print(player2 + " Wins")
        break
    elif b > highScore:
        b =b-dice2
    print(player2 + "'s total score " + str(b) )
time.sleep(2)
print("Hope u enjoyed my universe")
time.sleep(2)
print("Thank u")
time.sleep(5)