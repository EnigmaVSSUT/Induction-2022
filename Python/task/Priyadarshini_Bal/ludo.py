import random
value=True
while (value):
     PLAYER_1 = input("1st player's name:  ")
     PLAYER_2 = input("2nd player's name:  ")
     GOAL = int(input("Enter the goal:  "))
     s1 = s2 = 0
     
    
     while (value):
        
         if (s1 < GOAL) and (s2 < GOAL):
            
             input("press ENTER to roll the dice.")
             d1 = int(random.randint(1, 6))
             print("Dice value is: ",d1)
             s1 = s1+d1
             if s1 > GOAL:
                 s1 = s1-d1
             
             
             input("press ENTER to roll the dice.")
             d2 = int(random.randint(1, 6))
             print("Dice value is: ",d2)
             s2 = s2+d2
             if s2 > GOAL:
                 s2 = s2-d2
            
             print(f"{PLAYER_1}'s Score: {s1}","    ",f"{PLAYER_2}'s Score: {s2}")

        

        

         if s2 == GOAL:
             print(f"{PLAYER_2} you won the game!!")
             break

         if s1 == GOAL:
             print(f"{PLAYER_1} you won the game!!")
             break

     ASK_PLAYER = input("want to play again??? Then press a : ")

     if ASK_PLAYER.upper() == "a":
         continue
     else:
         print("Thank you for playing!!")
         break
