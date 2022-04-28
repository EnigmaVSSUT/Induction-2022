#Dice Roll game
import random as r
while True:
    try:
        goal=int(input('Enter the GOAL: '))
        if goal<1: 0/0
        score_1=score_2=0
        turn=1
        
        while True:
            print('\nTurn:',turn)
            turn+=1
            x=input('Player_1 press "ENTER" to roll the dice. ')
            a=r.randint(1,6)
            print('\tYou got',a)
            if score_1+a<=goal:
                score_1+=a
            print('\tSCORE =',score_1)
            
            x=input('Player_2 press "ENTER" to roll the dice. ')
            b=r.randint(1,6)
            print('\tYou got',b)
            if score_2+b<=goal:
                score_2+=b
            print('\tSCORE =',score_2)
            
            if score_1==goal and score_2!=goal:
                print('\nPlayer_1 is the winner!!!')
                break
            elif score_2==goal and score_1!=goal:
                print('\nPlayer_2 is the winner!!!')
                break
            elif score_1==goal and score_2==goal:
                print("\nIt's a tie!!!")
                break
            
    except:
        print('Invalid goal, try again.')
    choice=input('\nPress "q" or "Q" to quit the game: ')
    if choice in ('q','Q'):
        break
print('\nTHANK YOU for playing this game!!!')
        
        
