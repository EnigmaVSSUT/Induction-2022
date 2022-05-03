import random
goal=50
a=0
b=0
def randnum():
	c=random.randint(1,6)
	return c
while(a!=50 or b!=50):
	print("Player A turns")
	d=input("press y : ")
	if(d=="y"):
		outcome=randnum()
		print("Player A choice : ", outcome)
		a+=outcome
		if a==goal:
			print("A wins")
			break
		elif a>goal:
			a-=outcome
		print("A present score : ",a)
	print("Player B turns")
	e=input("press y : ")
	if(e=="y"):
		outcome=randnum()
		print("Player B choice : ", outcome)
		b+=outcome
		if b==goal:
			print("B wins")
			break
		elif b>goal:
			b-=outcome
		print("B present score : ",b)