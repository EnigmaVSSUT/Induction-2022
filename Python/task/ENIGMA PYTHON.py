import random
import time
s1=0
s2=0
s= int(input("Enter the score to be reached to win the game of dice\n"))
while (s1<s) and (s2<s):
    input("PLAYER_1-press enter to roll the dice")
    d1=int(random.randint(1,6))
    time.sleep(1)
    s1=s1+d1
    print(d1)
    if s1> s :
        s1=s1-d1
    if s1==s :
        print("PLAYER_1,CONGRATS!! YOU WON THE GAME")
        break
    input("PLAYER_2-press enter to roll the dice")
    d2=int(random.randint(1,6))
    time.sleep(1)
    d2=s2+d2
    print(d2)
    if s2>s :
        s2=s2-d2
    if s2==s :
        print("PLAYER_2,CONGRATS!! YOU WON THE GAME")
        break
