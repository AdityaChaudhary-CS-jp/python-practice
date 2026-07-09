# Problem127
a=int(input('Enter the number = '))
k=0
d=1
while a!=0:
    r=a%10
    a=a//10
    k=k+r
    d=d*r
if k==d:
    print('Spy number')
else:
    print('Not Spy number')
