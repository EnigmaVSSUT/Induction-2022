import random
g=int(input("enter goal score:"))
player1=input("enter player_1 name:")
player2=input("enter player_2 name:")
score1=0
score2=0
def dice():
    return random.randint(1,6)

while score1<=g and score2<=g:
    player1roll=dice()
    score1+=player1roll 
    print("score1",score1)

    if score1<=g:
       
        if score1==g:
            print("score1",score1)
            print(" congratulations!!!",player1,"wins") 
            break
    
    player2roll=dice()
    score2+=player2roll
    print("score2",score2)
   
    if score2<=g:
      
     if score2==g:
         print("score2",score2 )
         print(" congratulations!!!",player2,"wins")
         break
     
    if score1>g:
        score1=score1-player1roll
             
    if score2>g:
        score2=score2-player2roll
