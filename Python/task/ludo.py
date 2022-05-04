import random
goal =int(input("enter the goal"))
Player1=0
Player2=0
while (Player1!=goal or Player2!=goal):
 print("Player 1 turn")
 input ("Enter=dice rolls")
 roll1=int(random.randint(1,6))
 print("player 1 rolled",roll1)
 Player1=Player1+roll1
 if Player1 == goal:
  print("player 1 wins")
  break
 if Player1>goal:
  Player1-=roll1
 print("player 1 score is",Player1)
 print("Player 2 turn")
 input ("Enter=dice rolls")
 roll2=int(random.randint(1,6))
 print("player 2 rolled",roll2)
 Player2=Player2+roll2
 if Player2 == goal:
  print("player 2 wins")
  break
 if Player2>goal:
  Player2-=roll2
 print("player 2 score is",Player2)