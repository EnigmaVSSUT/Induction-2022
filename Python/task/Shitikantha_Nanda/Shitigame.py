import random

p1 = 0
p2 = 0
g = int(input("Enter the points to win the game:\n"))

while (p1 < g) and (p2 < g):
    input("Player 1 - Roll")
    e1 = int(random.randint(1, 6))
    p1 = p1 + e1
    print(e1)
    if p1 > g:
        p1 = p1 - g1
    if p1 == g:
        print("Congo Player 1 Wins!")
        break

    input("Player 2 - Roll!")
    e2 = int(random.randint(1, 6))
    p2 = p2 + e2
    print(e2)
    if p2 > g:
        p2 = p2 - e2
    if p2 == g:
        print("Congo Player 2 Wins!")
        break

    print("Player 1 Points: ", p1)
    print("Player 2 Points: ", p2)