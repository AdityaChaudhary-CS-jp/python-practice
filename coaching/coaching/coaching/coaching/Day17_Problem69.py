# Problem69
n = int(input('Enter a Table = '))
for i in range(n,n*10+1,n):
    print(i)

# AND
a = int(input('Enter a number = '))
b = int(input('Enter a term = '))

for m in range(1,b+1):
    print(a,'*',m,'=',a*m,sep='')
