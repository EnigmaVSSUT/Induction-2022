print("Welcome to ENIGMA's LUDO GAME PORTAL....")
import random
from random import randint
import time

player1 = input("Player 1 Please Enter your NAME :\n ") 
player2= input("Player 2 Please Enter your NAME :\n") 

def dicePlay(num_sides=6):
    """Returns number between 1 and 6 (inclusive)"""
    return random.randint(1,num_sides)

def playGame(playername):
    G = int(input("Enter a Score to reach to WIN the GAME : "))
    print("Hello,",player1 ,"and" ,player2,". Welcome to game of DICE! First to " ,G,"points wins!")
    p1score = 0
    p2score = 0
    while p1score != G and p2score != G: 
        print("The current score is: ",player1, p1score, "," ,player2 ,p2score)
        input("Please press 'Enter' to roll.")
        player1Roll = dicePlay()
        if(p1score+ player1Roll<=G) :
          p1score=p1score+ player1Roll
        else:
           p1score=p1score

        print("",player1,"'s dice rolled to.......... "+str(player1Roll)+".") 
        time.sleep(2)
        player2Roll = dicePlay()
        if(p2score+player2Roll<=G) :
          p2score=p2score+ player2Roll
        else:
           p2score=p2score
        print("",player2,"'s dice rolled to.......... "+str(player2Roll)+".")
        time.sleep(2)

    if p1score > p2score:
        print("Hurray!!" ,player1,"wins the game")
    elif (p1score == p2score):
        print("The game is Tied")
    else :
         print("Hurray!!" ,player2,"wins the game")

    if (p1score > p2score):
         return True
    else:
         return False
playerWins = playGame(player1)
if(playerWins== True):
  print("") 