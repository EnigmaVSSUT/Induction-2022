import random
target=int(input("Enter the target"))
score1=0
score2=0
x=0
y=0
while True:
    x=int(random.randint(1,6))
    score1=score1+x
    y=int(random.randint(1,6))
    score2=score2+y

    if (score1>target):
         score1=score1-x
    if (score2>target):
         score2=score2-y
    if (score1==target):
          print(f"Player 1 is the winner")
          break
    if (score2==target):
         print(f"Player 2 is the winner")
         break



    