import random
from random import randint


p1 = input("Enter the name of the first player ") 
p2 = input("Enter the name of the second player ") 

def diceRoll(n=6):

    return random.randint(1,n)

def playGameOfDice(p1):
    t = int(input("Enter a score to reach to win the game : "))
    p1Score = 0
    p2Score = 0
    while p1Score != t and p2Score != t: 
        print("The current score is: ",p1, p1Score ,p2 , p2Score)
        input("Press 'Roll' to roll the dice.")
        p1Roll = diceRoll()
        if(p1Score+p1Roll<=t):
            p1Score=p1Score+p1Roll
        else :
                p1Score=p1Score
        print("player 1's randomly selected number is  "+str(p1Roll)+".") 
        
        p2Roll = diceRoll()
        if(p2Score+p2Roll<=t):
            p2Score=p2Score+p2Roll
        else :
                p2Score=p2Score
        print("player 2's randomly selected number is  "+str(p2Roll)+".")
        
    if p1Score > p2Score:
        print("Congrats!" ,p1,"won the game")
    elif (p1Score == p2Score):
        print("It's Tie")
    else :
         print("Congrats!" ,p2,"won the game")

    if (p1Score > p2Score):
         return True
    else:
         return False
playerWins = playGameOfDice(p1)
if(playerWins== True):
  print("")
