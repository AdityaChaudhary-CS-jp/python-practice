# Problem128
a=int(input('Enter the number = '))
k=0
p=a
while a!=0:
    r=a%10
    a=a//10
    if r==0:
        print('Duck number')
        break
else:
        print('Not Duck number')
