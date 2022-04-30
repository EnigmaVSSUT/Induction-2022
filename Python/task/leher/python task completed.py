import random   
goal = int(input("Enter the goal : "))
list=[1,2,3,4,5,6]
score1 = 0
score2 = 0
while  (score1 < goal) and (score2 < goal):
        input(f"player1 press Enter to roll the dice.")
        dice1 = int(random.choice(list))
        print(f" rolled {dice1}")
        score1 = score1+dice1
        input(f"player2 press enter to roll the dice.")
        dice2 = int(random.choice(list))
        print(f" rolled {dice2}")
        score2 = score2+dice2
        if score1 > goal:
                score1 = score1-dice1
        if score2 > goal:
                score2 = score2-dice2
        print(f"player1's Score: {score1}\nplayer2's Score: {score2}")
        if score1 == goal:
                print(f"player1 wins")
                break
        if score2 == goal:
                print(f"player2 wins")
                break
