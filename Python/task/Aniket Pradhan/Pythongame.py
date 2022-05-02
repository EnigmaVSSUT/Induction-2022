import random
print("\nLUDO WORLD TM")
p1=input("\nEnter name of the first player:")
p2=input("\nEnter name of second player:")
w=int(input("\nEnter the winning point(score):"))
print("\n...")
score1=0
score2=0
while score1<w and score2<w:
    input("\n\n::PLAYER_1::\nPress Enter to roll dice...") 
    y=score1
    score1+=random.randint(1,6)
    print("Number on the dice:", score1-y)
    if score1>w:
        score1=y
    print("Player_1 score: ", score1)
    if score1==w:
        break
    input("\n\n::PLAYER_2::\nPress Enter to roll dice...")
    z=score2
    score2+=random.randint(1,6)
    print("Number on the dice:", score2-z)
    if score2>w:
        score2=z
    print("Player_2 score: ", score2)
    if score2==w:
        break
if score1==w:
    print("\nCONGRATULATIONS! Winner:", p1)
if score2==w:
    print("\nCONGRATULATIONS! Winner:", p2)
