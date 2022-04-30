import random

while True:
     firstplayer = input("First player enter your name ==> ")
     secondplayer = input("Second player  enter your name ==> ")
     target = int(input("Enter the target number: "))
     score1 = 0
     score2 = 0
     while True:
         if (score1 < target) and (score2 < target):
             input(f"{firstplayer} press enter to roll the dice.")
             dice1 = int(random.randint(1, 6))
             print(f"Dice rolled {dice1}")
             score1 = score1+dice1
             input(f"{secondplayer} press enter to roll the dice.")
             dice2 = int(random.randint(1, 6))
             print(f"Dice rolled {dice2}")
             score2 = score2+dice2
             print(f"{firstplayer}'s Score: {score1}\n{secondplayer}'s Score: {score2}")

         if score1 > target:
             score1 = score1-dice1

         if score2 > target:
             score2 = score2-dice2

         if score2 == target:
             print(f"{secondplayer} you won the game!!")
             break

         if score1 == target:
             print(f"{firstplayer} you won the game!!")
             break

     replay = input("Press y to play again or press any other key to exit ==> ")

     if replay.lower() == "y":
         continue
     else:
         print("Thank you for playing!!")
         break