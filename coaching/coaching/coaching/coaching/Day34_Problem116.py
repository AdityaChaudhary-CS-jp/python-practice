# Problem116
a=int(input('Enter the no = '))
k=0
while a!=0:
    r=a%10
    a=a//10
    k=k+1
print('It is',k,'digit number')
