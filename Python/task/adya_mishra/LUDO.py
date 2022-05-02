import random
goal=int(input("Enter the goal"));
score1=0;
score2=0;
c1=0;c2=0;
i=1;
while(i>0):
    
    c1=int(random.randint(1,6));
    c2=int(random.randint(1,6));
    print(f"Player 1 score: {c1} \nPlayer 2 score: {c2}");
    
    score1=score1+c1;
    score2=score2+c2;
    if(score1==goal):
      print("Player 1 Winner");
      break;
    if(score1>goal):
      score1=score1-c1;

    if(score2==goal):
        print("Player 2 Winner");
        break;
    if(score2>goal):
        score2=score2-c2;
    c1=0;c2=0;
    i=1;

    
      

    
  