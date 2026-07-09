# Problem124
a=int(input('Enter the number = '))
k=0
p=a
while a!=0:
    r=a%10
    a=a//10
    k=k+r
if p%k==0:
    print('It is Niven number')
else:
    print('It is not Niven number')
