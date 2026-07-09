# Problem125
a=int(input('Enter the number = '))
k=0
p=a**2
d=a
while p!=0:
    r=p%10
    p=p//10
    k=k+r
if d==k:
    print('Neon number')
else:
    print('Not Neon number')
