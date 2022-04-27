import random
g=int(input("enter the goal"))
s1=0
s2=0
c1=0
c2=0
i=1
while(i>0):
    c1=int(random.randint(1,6))
    c2=int(random.randint(1,6))
    print("score of player 1- {c1}  score of player 2- {c2}")

    s1+=c1
    s2+=c2
    if (s1==g):
        print("player 1 is the winner")
        break
    if(s1>g):
        s1=s1-c1

    if(s2==g):
        print("player 2is the winner")
        break
    if(s2>g):
        s2=s2-c2
    