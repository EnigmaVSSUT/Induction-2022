import random
from random import randint
import time

playerName = input("player 1 Please enter your name :\n ") 
playerName1= input("player 2 Please enter your name of:\n") 

def dicePlay(num_sides=6):
    """Returns number between 1 and 6 (inclusive)"""
    return random.randint(1,num_sides)

def playGame(playername):
    a = int(input("Enter a score to reach to win the game : "))
    print("Hello,",playerName ,"and" ,playerName1,". Welcome to game of dice! First to " ,a,"points wins!")
    p1score = 0
    p2score = 0
    while p1score != a and p2score != a: 
        print("The current score is: ",playerName, p1score, "," ,playerName1 ,p2score)
        input("Please press 'Enter' to roll.")
        player1Roll = dicePlay()
        if(p1score+ player1Roll<=a) :
          p1score=p1score+ player1Roll
        else:
           p1score=p1score

        print("",playerName,"'s dice rolled to.......... "+str(player1Roll)+".") 
        time.sleep(2)
        player2Roll = dicePlay()
        if(p2score+player2Roll<=a) :
          p2score=p2score+ player2Roll
        else:
           p2score=p2score
        print("",playerName1,"'s dice rolled to.......... "+str(player2Roll)+".")
        time.sleep(2)

    if p1score > p2score:
        print("Hurray!!" ,playerName,"wins the game")
    elif (p1score == p2score):
        print("The game is Tied")
    else :
         print("Hurray!!" ,playerName1,"wins the game")

    if (p1score > p2score):
         return True
    else:
         return False
playerWins = playGame(playerName)
if(playerWins== True):
  print("") 