import random
p1=input("Enter player 1 name:")
p2=input("Enter player 2 name:")
goal=input("Enter the goal: ")
print("#################")
y=0
z=0
cmplt=True
while(cmplt):
     print(f"{p1}'s turn:")
     x=input("Hit enter")
     s1=random.randint(1,6)
     print(f"{p1} scored :{s1}")
     y=y+s1
     if y==int(goal):
          print(f"congrats!! {p1} is the winner :)\n{p2} noob -_-\n")
          cmplt=False
          break
     if y<int(goal):
          print(f"Total score of {p1}:{y}\n")
     if(y>int(goal)):
          print(f"Sorry!! {y} exceeds {goal}")
          y=y-s1           
          print(f"Total score of {p1}:{y}\n")
     print("**********")
     print(f"{p2}'s turn:")
     x=input("Hit Enter")
     s2=random.randint(1,6)
     print(f"{p2} scored :{s2}")
     z=z+s2
     if z==int(goal):
          print(f"congrats!! {p2} is the winner :)\n{p1} noob -_-")
          cmplt=False
          break
     if z<int(goal):
          print(f"Total score of {p2}:{z}\n")
     if(z>int(goal)):
          print(f"Sorry!! {z} exceeds {goal}")
          z=z-s2           
          print(f"Total score of {p2}:{z}\n")
     print("**************")
print("Thanks for playing!!!")





