import random
goal=50
PLAYER_1=0
PLAYER_2=0
def randnum():
	c=random.randint(1,6)
	return c
while(PLAYER_1!=50 or PLAYER_2!=50):
	print("Player A turn")
	d=input("press y : ")
	if(d=="y"):
		outcome=randnum()
		print("your choice : ", outcome)
		PLAYER_1+=outcome
		if PLAYER_1==goal:
			print("PLAYER_1 wins")
			break
		elif PLAYER_1>goal:
			PLAYER_1-=outcome
		print("A present score : ",PLAYER_1)
	print("Player_B turn")
	e=input("press y : ")
	if(e=="y"):
		outcome=randnum()
		print("your choice : ", outcome)
		PLAYER_2+=outcome
		if PLAYER_2==goal:
			print("PLAYER_2 wins")
			break
		elif PLAYER_2>goal:
			PLAYER_2-=outcome
		print("B present score : ",PLAYER_2)