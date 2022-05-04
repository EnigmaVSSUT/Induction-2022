import random
print("Enter Player 1 name : ", end="")
p1 = input()
print("Enter player 2 name : ", end = "")
p2 = input()
print("Enter the target : ", end = "")
tar = int(input())
print("Press Enter Key to roll . . . .")
print("#####################")
print("#####################")

sum1 = 0
sum2 = 0
counter = 1
while(True):
    if counter%2 != 0:
        print(p1,"...roll  ", end = "")
        k = input()
        K1 = random.randrange(1,7)
        print(p1,"Current toss : ",K1)
        if sum1<tar and sum1+K1 <= tar:
            sum1 = sum1 + K1
        print(p1,"Total points: ", sum1)
        print("---------------------")
        
    else:
        print(p2,"...roll  ", end = "")
        k = input()
        K2 = random.randrange(1,7)
        print(p2,"Current toss :",K2)
        if sum2<tar and sum2+K2<= tar:
            sum2 = sum2 + K2
        print(p2,"Total points: ", sum2)
        print("---------------------")
    
    if sum1 == tar:
        print("---------------------")
        print("Player",p1,"Wins!")
        print("Total Points : ", sum1)
        print("Last Toss : ",K1)
        print("---------------------")
        print("---------------------")
        break
    elif sum2==tar:
        print("---------------------")
        print("Player",p2,"Wins!")
        print("Total Points : ", sum2)
        print("Last Toss : ",K2)
        print("---------------------")
        print("---------------------")
        break
    else:
        counter +=1
        continue

