import random
goal=50
a=0
b=0
def randnum():
	c=random.randint(1,6)
	return c
while(a!=50 or b!=50):
	print("Turn : A")
	outcome=randnum()
	print("Dice Rolls As : ", outcome)
	a+=outcome
	if a==goal:
		print("Winner is A")
		break
	elif a>goal:
		a-=outcome
	print("Score after Adding previous one : ",a)
	print("Turn : B")
	outcome=randnum()
	print("Dice Rolls As : ", outcome)
	b+=outcome
	if b==goal:
		print("Winner is B")
		break
	elif b>goal:
		b-=outcome
	print("Score after Addding previous one : ",b)