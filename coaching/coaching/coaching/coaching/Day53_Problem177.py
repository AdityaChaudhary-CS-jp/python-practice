# Problem177
a = int(input('How many Numbers = '))
b = []
for i in range(a):
    print('Enter',i+1,'Number',end=' ')
    c  = int(input('='))
    b.append(c)
print(b)
d = int(input('Enter any number = '))
if d in b :
    print('Number is in list')
    print('Its Position is = ', b.index(d) + 1)
else:
    print('Not in List')
