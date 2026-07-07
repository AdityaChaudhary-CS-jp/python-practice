# Problem118
a=int(input('Enter the no = '))
k=0
while a!=0:
    r=a%10
    a=a//10
    k=k*10+r
print('Reverse no = ',k)
