# Problem130
a=int(input('Enter the number = '))
d=a
k=0
p=a**2
while a!=0:
    a=a//10
    k=k+1
l=10**k
c=p%l
if d==c:
    print('Automorphic Number')
else:
    print('Not Automorphic Number')
