# Problem123
a=int(input('Enter the number= '))
p=a
d=p
k=0
while a!=0:
    a=a//10
    k=k+1
print(k,'Digit number')
m=0
while p!=0:
    r=p%10
    p=p//10
    m=r**k+m
if m==d:
        print('Armstrong Number')
else:
        print('Not Armstrong Number')
