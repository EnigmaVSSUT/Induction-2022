import random
from random import randint
import time
p1 = input("Enter First Player's name== ") 
p2 = input("Enter Second Player's name== ") 

def roll(n=6):

 return random.randint(1,n)

def game(p1):
    s = int(input("Input a score that needs to be reached to win the game : "))
    p1score = 0
    p2score = 0
    while (p1score <= s and p2score <= s): 
        print("The current score is: ",p1, p1score ,p2, p2score)
        input("Press 'enter' to roll the dice")
        p1Roll = roll()
        if(p1score+p1Roll<=s):
            p1score=p1score+p1Roll
        else :
                p1score=p1score
        print("player one's rolled number is  "+str(p1Roll)+".")
        time.sleep(1)
        p2Roll = roll()
        if(p2score+p2Roll<=s):
            p2score=p2score+p2Roll
        else :
                p2score=p2score
        print("player two's rolled number is  "+str(p2Roll)+".")
        time.sleep(1)

        
    if p1score > p2score:
        print("Congrats!!!" ,p1,",you won the game")
    elif (p1score == p2score):
        print("It's Tie")
    else :
         print("Congrats!!!" ,p2,",you won the game")