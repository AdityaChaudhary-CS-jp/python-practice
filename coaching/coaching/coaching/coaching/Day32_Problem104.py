# Problem104
a = int(input("How many rows = "))
for i in range(a):
    for j in range(a-i-1):
        print(' ',end=' ')
    for k in range(i+1):
            print('*',end=' ')
    for l in range(i):
        print('*',end=' ')
    print()
