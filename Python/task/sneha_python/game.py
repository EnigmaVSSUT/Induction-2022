import random
g=int(input("enter goal score:"))
player1=input("enter player_1 name:")
player2=input("enter player_2 name:")
print(".........GAME START.........")
score1=0
score2=0
def dice():
    return random.randint(1,6)

while score1<=g and score2<=g:
    player1roll=dice()
    print(f"{player1} scored :{score1}")
    score1+=player1roll
     
    #print(player1,"score1:",score1)
    print("****************")

    if score1<=g:
       
        if score1==g:
            #print(player1,"score1:",score1)
            print(f"{player1} scored :{score1}")
            print("****************")
            print(" congratulations!!!",player1,"wins") 
            print("..................................")
            print("THANK YOU FOR PLAYING!!!")
            break
        
    player2roll=dice()
    print(f"{player2} scored :{score2}")
    score2+=player2roll
    #print(player2,"score2",score2)
    print("****************")
   
    if score2<=g:
      
     if score2==g:
         print(f"{player2} scored :{score2}")
         #print(player2,"score2:",score2 )
         print("****************")
         print(" congratulations!!!",player2,"wins")
         print("..................................")
         print("THANK YOU FOR PLAYING!!!")
         break
     
    if score1>g:
        score1=score1-player1roll
             
    if score2>g:
        score2=score2-player2roll
