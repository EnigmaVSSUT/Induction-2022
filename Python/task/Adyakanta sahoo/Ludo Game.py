import random
Participant_1 = input("Participant 1 name is : ")
Participant_2 = input("Participant 2 name is : ")
goal = int(input("Target for both players to reach goal : "))
Total_Points_1 = 0
Total_Points_2 = 0
ptr = 1
compete = True
while(compete):
    if ptr%2 == 0:
        print(Participant_2,"turn ", end = "")
        throw = input()
        temp2 = random.randint(1,6)
        print(Participant_2,"Dice Threw :",temp2)
        if Total_Points_2<goal and Total_Points_2+temp2<= goal:
            Total_Points_2 = Total_Points_2 + temp2
        print("Total score earned ", Total_Points_2,"\n")
    else:
        print(Participant_1,"turn " ,end = "")
        throw = input()
        temp = random.randint(1,6)
        print(Participant_1,"Dice threw : ",temp)
        if Total_Points_1<goal and Total_Points_1+temp <=goal:
            Total_Points_1 = Total_Points_1 + temp
        print("Total points earned: ", Total_Points_1,"\n")
    if Total_Points_1 == goal:
        print("Winner is : ",Participant_1)
        break
    elif Total_Points_2==goal:
        print("Winner is : ",Participant_2)
        break
    else:
        ptr +=1
print("Game is sucessfully Over")
print("-------------------------")