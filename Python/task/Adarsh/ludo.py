import random
goal=50
a=0
b=0
def randnum():
	c=random.randint(1,6)
	return c
while(a!=50 or b!=50):
	print("Turn: A")
	d=input("press z : ")
	if(d=="z"):
		outcome=randnum()
		print("Dice Roll's As : ", outcome)
		a+=outcome
		if a==goal:
			print("Winner: A")
			break
		elif a>goal:
			a-=outcome
		print("Score after Adding previous one : ",a)
	print("Turn: B")
	e=input("press a : ")
	if(e=="a"):
		outcome=randnum()
		print("Dice Roll's As : ", outcome)
		b+=outcome
		if b==goal:
			print("Winner: B")
			break
		elif b>goal:
			b-=outcome
		print("Score after Adding previous one : ",b)
