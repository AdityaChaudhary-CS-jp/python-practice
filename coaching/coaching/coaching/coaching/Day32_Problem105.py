# Problem105
a = int(input("How many rows = "))
for i in range(a):
    for j in range(i):
        print(' ',end=' ')
    for k in range(a-i):
        print('*',end=' ')
    for l in range(a-1-i):
        print('*',end=' ')
    print() 
