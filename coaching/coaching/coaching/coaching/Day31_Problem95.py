#Problem95
a=int(input('How many rows = '))
b =int(input('How many columns = '))
for i in range(1,a+1):
    print('@',end= ' ')
    for j in range(1,b+1):
        print('-',end=' ')
    print(i,end=' ')
    print()
