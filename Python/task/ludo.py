import random
# t is the target for the game
t = int(input("target is:-"))
 #s1,s2 are the scores of player1 and player2
s1=0
s2=0
while (s1<t) and (s2<t):
    #here two players rolling their dice alternatively and their score will be added to their previous score
    input("player_1 press enter to roll the dice")
    dice1=int(random.randint(1,6))
    s1=s1+dice1
    print(dice1)
    input("Player_2 press enter to roll the dice")
    dice2=int(random.randint(1,6))
    dice2=s2+dice2
    print(dice2)
    #if score will exceed the target then recently generated score will be discarded
    #winner will be declared only if player score is equal to target
    if s1> t :
        s1=s1-dice1
    if s1==t :
        print("Player_1 is the winner")
        break

    if s2>t :
        s2=s2-dice2
    if s2==t :
        print("Player_2 is the winner")
        break
