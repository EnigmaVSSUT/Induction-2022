import random
goal=int(input("enter a goal"))
score1=0
score2=0
x=0
y=0
i=1
while(i>0):
    x=int(random.randint(1,6))
    y=int(random.randint(1,6))
    print("Player1 score={x} Player2 score={y}")
    score1=score1+x
    score2=score2+y
    if(score1==goal):
        print("Player 1 is the Winner !!!")
        break
    if(score1>goal):
        score1==score1-x
    if(score2==goal):
        print("Player 2 is the Winner !!!")
        break
    if(score2>goal):
        score2=score2-y    
    x=0;y=0
    i=1
