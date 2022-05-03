import random
target  = int(input("Enter the target:\n"))
p1 = 0
p2 = 0

while(p1 < target and p2 < target):
    print("player 1 hit any key to roll the dice:\n")
    d1 = int(random.randint(1,6))
    print(d1)
    p1 = p1 + d1

    print("player 2 hit any key to roll the dice:\n")
    d2 = int(random.randint(1,6))
    print(d2)
    p2 = p2 + d2

    if(p1 > target):
        p1 = p1 - d1
    if(p1 == target):
        print("p1 wins!")
        break

    if(p2 > target):
        p2 = p2 - d2
    if(p2 == target):
        print("p2 wins!")
        break

    



