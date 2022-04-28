import random
target=int(input("Enter the target"));
score1=0;
score2=0;
a=0;b=0;
i=1;
while(i>0):

    a=int(random.randint(1,6));
    b=int(random.randint(1,6));
    print(f"Player1's score: {a} \n Player2's score: {b}");

    score1=score1+a;
    score2=score2+b;
    if(score1==target):
      print("Player1 is the winner");
      break;
    if(score1>target):
      score1=score1-a;

    if(score2==target):
        print("Player2 is the winner");
        break;
    if(score2>target):
        score2=score2-b;
    a=0;b=0;
    i=1;





