# Problem136
a=int(input('Enter the number = '))
c=a
b=a
while a!=0:
    r=a%10
    a=a//10
    b=c
    e=0
    while b!=0:
        if b%10==r:
            e+=1
        b//=10
    if e>1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')
