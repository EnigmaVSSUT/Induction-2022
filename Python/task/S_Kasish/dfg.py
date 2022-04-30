import random

goal=int(input("Enter the goal:"))
score1,score2=0,0
player1,player2=0,0
i=1

while(i>0):
    player1=int(random.randint(1,6))
    player2=int(random.randint(1,6))
    print(f"player 1 score: {player1} \nplayer 2 score: {player2}")
    score1+=player1
    score2+=player2

    if(score1>goal):
        print("Player 1 Winner")
        break
    if(score1>goal):
        score1-=player1

    if(score2==goal):
        print("Player 2 Winner")
        break
    if(score2>goal):
        score2-=player2
    
    player2,player1=0,0
    i=1