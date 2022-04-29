import random
PLAYER1=input("ENTER THE NAME OF PLAYER1 :==>")
PLAYER2=input("ENTER THE NAME OF PLAYER2 :==>")
TARGET=input("ENTER THE TARGET YOU WANT TO PLAY: ")
TOTAL_S1=0
TOTAL_S2=0
game=True
while(game):
     print(f"{PLAYER1}'s turn:")
     K=input("press enter")
     J1=random.randint(1,6)
     print(f"{PLAYER1} scored :{J1}")
     TOTAL_S1=TOTAL_S1+J1
     if TOTAL_S1==int(TARGET):
          print(f"congrats!!!!! {PLAYER1} is the winner_pro :)\n{PLAYER2} hacker \n")
          game=False
          break
     if TOTAL_S1<int(TARGET):
          print(f"Total score of {PLAYER1}:{TOTAL_S1}\n")
     if(TOTAL_S1>int(TARGET)):
          print(f"Sorry!! {TOTAL_S2} exceeds {TARGET}")
          TOTAL_S1=TOTAL_S1-J1          
          print(f"Total score of {PLAYER1}:{TOTAL_S1}\n")
     print(f"{PLAYER2}'s turn:")
     k=input("press enter")
     J2=random.randint(1,6)
     print(f"{PLAYER2} scored :{J2}")
     TOTAL_S2=TOTAL_S2+J2
     if TOTAL_S2==int(TARGET):
          print(f"congrats!!!!!! {PLAYER2} is the winner_pro :)\n{PLAYER1} hacker")
          game=False
          break
     if TOTAL_S2<int(TARGET):
          print(f"Total score of {PLAYER2}:{TOTAL_S2}\n")
     if(TOTAL_S2>int(TARGET)):
          print(f"Sorry!! {TOTAL_S2} exceeds {TARGET}")
          TOTAL_S2=TOTAL_S2-J2          
          print(f"Total score of {PLAYER2}:{TOTAL_S2}\n")
     print("#####################")
print("!!!!!Thanks for playing!!!!!!")