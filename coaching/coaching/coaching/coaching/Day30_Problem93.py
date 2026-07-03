# Problem93
a = int(input('How many rows = '))
b = int(input('How many column = '))
p = ord('a')
for i in range(1,a+1):
    for j in range(1,b+1):
        
        print(chr(p),end= ' ')
        p=p+1
    print()
