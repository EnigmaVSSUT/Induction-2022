import random
goal=input("Enter the goal: ")
print("#################")
m=0
n=0
cmplt=True
while(cmplt):
     print(f"player 1's turn:")
     x=input("Hit enter")
     s1=random.randint(1,6)
     print(f"player 1 scored :{s1}")
     m=m+s1
     if m==int(goal):
          print(f"congrats!! player 1 is the winner :)\nplayer 2 noob -_-\n")
          cmplt=False
          break
     if m<int(goal):
          print(f"Total score of player 1:{m}\n")
     if(m>int(goal)):
          print(f"Sorry!! {m} exceeds {goal}")
          m=m-s1           
          print(f"Total score of player 1:{m}\n")
     print("**********")
     print(f"player 2's turn:")
     x=input("Hit Enter")
     s2=random.randint(1,6)
     print(f"player 2 scored :{s2}")
     n=n+s2
     if n==int(goal):
          print(f"congrats!! player 2 is the winner :)\nplayer 1 noob -_-")
          cmplt=False
          break
     if n<int(goal):
          print(f"Total score of player 2:{n}\n")
     if(n>int(goal)):
          print(f"Sorry!! {n} exceeds {goal}")
          n=n-s2           
          print(f"Total score of player 2:{n}\n")
     print("**************")
print("Thanks for playing!!!")





