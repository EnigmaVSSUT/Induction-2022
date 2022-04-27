import random
from random import randint


p1Name = input("enter 1st player's name ") 
p2Name = input("enter 2nd player's name ") 


def dicevalue():
    return random.randint(1,6)

def GameOfDice(p1Name):
    g = int(input("Enter goal score : "))
    s1 = 0
    s2 = 0
    while s1 != g and s2 != g: 
        print("The current score is: ",p1Name,"=", s1 ,"   ",p2Name ,"=", s2)
        input("enter roll")
        p1Roll = dicevalue()
        if(s1+p1Roll<=g):
            s1=s1+p1Roll
        else :
                s1=s1
        print("player 1's randomly selected number is  "+str(p1Roll)+".") 
    
        p2Roll = dicevalue()
        if(s2+p2Roll<=g):
            s2=s2+p2Roll
        else :
                s2=s2
        print("player 2's randomly selected number is  "+str(p2Roll)+".")
        
    if s1 > s2:
        print("Congrats!" ,p1Name,"won the game")
    elif (s1 == s2):
        print("It's Tie")
    else :
         print("Congrats!" ,p2Name,"won the game")

    if (s1 > s2):
         return True
    else:
         return False
playerWins = GameOfDice(p1Name)
if(playerWins== True):
  print("")