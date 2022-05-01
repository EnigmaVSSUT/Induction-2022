import random
goal = int(input("enter goal value:\n"))
p1 = 0
p2 = 0
while (p1<goal and  p2<goal):

    print(" player 1 press any key to roll the dice:\n")
    d1 = int (random.randint (1,6))
    print(d1)
    
    p1 = p1 + d1
    



    print(" player 2 press any key to roll the dice:\n")
    d2 = int (random.randint (1,6))
    print(d2)
    
    p2 = p2 + d2
    
    
    if(p1>goal):
        p1 = p1 -d1
    if (p1== goal):
        print("p1 wins") 
        break   

    if(p2>goal):
        p2 = p2 -d2
    if (p2== goal):
        print("p2 wins")   
        break 
