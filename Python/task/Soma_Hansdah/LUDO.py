import random
target=int(input("Enter Goal\n"))
P1=0
P2=0
while(P1<target) and (P2<target) :

    print("P1 Press ENTER to roll the dice\n")
    dice1=int(random.randint(1,6))
    P1=P1+dice1

    if(P1>target) :
      
          P1=P1-dice1
      
    if(P1==target) :
      
          print("P1 WINS!!")
          break
      
    
    print("P2 Press ENTER to roll the dice\n")
    dice2=int(random.randint(1,6))
    P2=P2+dice2

    if(P2>target) :
       
            P2=P2-dice2
       
    if(P2==target) :
       
            print("P2 WINS!!")
            break
       
