import random

while True:
    player1 = input("Player 1 name : ")
    player2 = input("Player 2 name : ")
    goal = int(input("Enter your goal : "))
  
    s1 = 0
    s2 = 0
    
    while True:
        if (s1 < goal) and (s2 < goal):
            input(f"{player1} press Enter to roll the dice -")
            roll1 = int(random.randint(1, 6))
           
            print(f"It rolled {roll1}")
            s1 = s1+roll1
           
            input(f"{player2} press enter to roll the dice -")
            roll2 = int(random.randint(1, 6))

            print(f"It rolled {roll2}")
            s2 = s2+roll2
           
            print(f"{player1}'s Score: {s1}\n{player2}'s Score: {s2}")

        if s1 > goal:
            s1 = s1-roll1

        if s2 > goal:
            s2 = s2-roll2

        if s1 == goal:
            print(f"{player1} is the Winner")
            break

        if s2 == goal:
            print(f"{player1} is the Winner")
            break

    X = input("Enter A to replay or any other key to Exit :")

    if X.lower() == "a":
        continue
    
    else:
        print("O(∩_∩)O  Thank you for playing  O(∩_∩)O")
        break

    
