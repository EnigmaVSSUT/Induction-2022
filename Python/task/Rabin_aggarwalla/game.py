import random
p1=input("Enter player 1 name:")
p2=input("Enter player 2 name:")
goal=input("Enter the goal: ")
print("$$$$$$$$$$$$$$$$")
y=0
z=0
cmplt=True
while(cmplt):
     print(f"{p1}'s turn:")
     x=input("press enter")
     s1=random.randint(1,6)
     print(f"{p1} scored :{s1}")
     y=y+s1
     if y==int(goal):
          print(f" {p1} is the winner :)\n{p2} lost\n")
          cmplt=False
          break
     if y<int(goal):
          print(f"Total score of {p1} is :{y}\n")
     if(y>int(goal)):
          print(f"Sorry {y} is more than {goal}")
          y=y-s1           
          print(f"Total score of {p1}:{y}\n")
     print("###########")
     print(f"{p2}'s turn:")
     x=input("press Enter")
     s2=random.randint(1,6)
     print(f"{p2} scored :{s2}")
     z=z+s2
     if z==int(goal):
          print(f"congrats!! {p2} is the winner :)\n{p1} lost")
          cmplt=False
          break
     if z<int(goal):
          print(f"Total score of {p2}:{z}\n")
     if(z>int(goal)):
          print(f"sorry {z} is more than {goal}")
          z=z-s2           
          print(f"Total score of {p2}:{z}\n")
     print("#################")
print("Game completed")





