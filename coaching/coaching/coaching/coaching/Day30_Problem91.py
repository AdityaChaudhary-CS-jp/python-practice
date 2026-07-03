# Problem91
a = int(input('How many rows = '))
b = int(input('How many column = '))
for i in range(a,0,-1):
    for j in range(b,0,-1):
        print(j,end=' ')
    print()
