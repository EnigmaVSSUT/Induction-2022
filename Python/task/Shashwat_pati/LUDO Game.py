import random
total=50
a=0
b=0
def randnum():
	c=random.randint(1,6)
	return c
while(a!=50 or b!=50):
	print("Player A's turn--")
	d=input("Press y/Y to roll dice : ")
	if(d=="y" or d=="Y"):
		outcome=randnum()
		print("Dice rolled : ", outcome)
		a+=outcome
		if a==total:
		    print("         No MORE ROLLING, BYE BYE")
		    print("         :::---    A wins  ---:::")
		    print("         <|>     GAME OVER    <|>")
		    break
		elif a>total:
			a-=outcome
		print("A present score : ",a)
	print("Player B's turn--")
	e=input("press y : ")
	if(e=="y" or e=="Y"):
		outcome=randnum()
		print("Dice rolled : ", outcome)
		b+=outcome
		if b==total:
		    print("        No MORE ROLLING, BYE BYE")
		    print("        :::---   B wins  ---:::")
		    print("        <|>    GAME OVER    <|>")
		    break
		elif b>total:
			b-=outcome
		print("B present score : ",b)
		print("\n")
