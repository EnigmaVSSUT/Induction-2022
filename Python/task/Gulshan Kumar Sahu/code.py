import random
from random import randint


def rolldise():
    return random.randint(1,6)


player1 = input("Name of player 1:")
player2 = input("Name of player 2:")
target = int(input('Enter the score to WIN:'))
score1 = 0
score2 = 0
print("the current score:")
print(player1,"->",score1)
print(player2,"->",score2)

while score1!=target and score2!=target:
    tmpsco1 = rolldise() 
    if score1 + tmpsco1 <= target:
        score1+=tmpsco1
    print(player1,"'s dise rolls to ",tmpsco1)
    tmpsco2 = rolldise()
    if score2 + tmpsco2 <= target:
        score2+=tmpsco2
    print(player2,"'s dise rolls to ",tmpsco2)
    print("the current score:")
    print(player1,"->",score1)
    print(player2,"->",score2)
    input("press Enter to continue:")

if score1==target:
    print(player1," is the WINNER.")
else:
    print(player2," is the WINNER.")


