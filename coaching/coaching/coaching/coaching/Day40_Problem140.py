# Problem140
a=input('Enter the name = ')
b=int(input('Enter the position number = '))
c=len(a)
if b<=c:
    print(a[b-1])
else:
    print('INVALID POSITION')
