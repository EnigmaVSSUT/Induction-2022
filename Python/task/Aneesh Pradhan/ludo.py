import random
goal=50
a=0
b=0
def randnum():
	c=random.randint(1,6)
	return c
while(a!=50 or b!=50):
	print("Player A turn")
	d=input("press y : ")
	if(d=="y"):
		outcome=randnum()
		print("your choice : ", outcome)
		a+=outcome
		if a==goal:
			print("PLAYER_1 wins")
			break
		elif a>goal:
			a-=outcome
		print("A present score : ",a)
	print("Player_B turn")
	e=input("press y : ")
	if(e=="y"):
		outcome=randnum()
		print("your choice : ", outcome)
		b+=outcome
		if b==goal:
			print("PLAYER_2 wins")
			break
		elif b>goal:
			b-=outcome
		print("B present score : ",b) 