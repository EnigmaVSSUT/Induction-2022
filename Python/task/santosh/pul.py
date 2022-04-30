import random

p1 = 0
p2= 0
goal = int(input("Enter the target:\n"))

while (p1 < goal) and (p2< goal):
    input("Player 1 - Hit Enter to roll Dice!")
    d1 = int(random.randint(1, 6))
    p1 = p1 + d1
    print(d1)
    if p1 > goal:
        p1 = p1 - d1
    if p1 == goal:
        print("Player 1 Wins")
        break

    input("Player 2 - Hit Enter to roll Dice!")
    d2 = int(random.randint(1, 6))
    p2 = p2 + d2
    print(d2)
    if p2 > goal:
        p2 = p2 - d2
    if p2 == goal:
        print("Player 2 Wins")
        break

    print("Player 1 Score: ", p1)
    print("Player 2 Score: ", p2)
