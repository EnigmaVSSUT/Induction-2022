import random   
goal = int(input("Enter goal : "))
list=[1,2,3,4,5,6]
s1 = 0
s2 = 0
while  (s1 < goal) and (s2 < goal):
        input(f"Player_1 press Enter to roll the dice.")
        d1 = int(random.choice(list))
        print(f" rolled {d1}")
        s1 = s1+d1
        input(f"Player_2 press enter to roll the dice.")
        d2 = int(random.choice(list))
        print(f" rolled {d2}")
        s2 = s2+d2
        if s1 > goal:
                s1 = s1-d1
        if s2 > goal:
                s2 = s2-d2
        print(f"Player_1 Score: {s1}\nPlayer_2 Score: {s2}")
        if s1 == goal:
                print(f"Player_1 wins")
                break
        if s2 == goal:
                print(f"Player_2 wins")
                break