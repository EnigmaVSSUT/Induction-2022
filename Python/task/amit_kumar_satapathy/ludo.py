import random
goal=10
a=0
b=0
def randomno():
 c=random.randint(1,6)
 return c
while(a!=10 or b!=10):
 print("player A try your luck :")
 d=input("type r to roll : ")
 if(d=="r"):
  result=randomno()
  print("your choice : ", result)
  a+=result
  if a==goal:
   print("player A is the winner")
   break
  elif a>goal:
   a-=result
  print("till now score score of A is = ",a)
 print("Player B")
 e=input("type r to roll : ")
 if(e=="r"):
  result=randomno()
  print("your choice : ", result)
  b+=result
  if b==goal:
   print("player B is the winner,congratulations")
   break
  elif b>goal:
   b-=result
  print("till now the score of B is =  ",b)
