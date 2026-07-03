# Problem92
a = int(input('How many rows = '))
b = int(input('How many column = '))
c=ord('a')
for i in range(1,a+1):
    for j in range(1,b+1):
        print(chr(c),end=' ')
    print()
    c=c+1
