import random
g=input('Goal: ')
g=int(g)
p1=0
p2=0
while 0==0:
    x=input('\nPlayer-1 press enter')
    a=random.randint(1,6)
    print('Dice rolled to',a)
    if p1+a<=g:
        p1+=a
    print('Score=',p1)
    x=input('\nPlayer-2 press enter')
    b=random.randint(1,6)
    print('Dice rolled to',b)
    if p2+b<=g:
        p2+=b
    print('Score=',p2)
    if p1==g and p2!=g:
        print('\nPlayer-1 is winner')
        break
    elif p2==g and p1!=g:
        print('\nPlayer-2 is winner')
        break
    elif p2==g and p1==g:
        print('\nMATCH TIED')
        break
