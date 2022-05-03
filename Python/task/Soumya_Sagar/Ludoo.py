import random
Player_2 = input("Player 1 name : ")
Player_1 = input("Player 2 name : ")
Destined_Number = int(input("Destined target : "))
Total_Points_1 = 0
Total_Points_2 = 0
ChackTab = 1
flag = True
while(flag):
    if ChackTab%2 == 0:
        print(Player_2,"turn ", end = "")
        passOn = input()
        temp2 = random.randint(1,6)
        print(Player_2,"Dice Threw :",temp2)
        if Total_Points_2<Destined_Number and Total_Points_2+temp2<= Destined_Number:
            Total_Points_2 = Total_Points_2 + temp2
        print("Total points earned ", Total_Points_2,"\n")
    else:
        print(Player_1,"turn " ,end = "")
        passOn = input()
        temp1 = random.randint(1,6)
        print(Player_1,"Dice threw : ",temp1)
        if Total_Points_1<Destined_Number and Total_Points_1+temp1 <= Destined_Number:
            Total_Points_1 = Total_Points_1 + temp1
        print("Total points earned: ", Total_Points_1,"\n")
        
    
    if Total_Points_1 == Destined_Number:
        print("Winner : ",Player_1)
        break
    elif Total_Points_2==Destined_Number:
        print("Winner : ",Player_2)
        break
    else:
        ChackTab +=1

