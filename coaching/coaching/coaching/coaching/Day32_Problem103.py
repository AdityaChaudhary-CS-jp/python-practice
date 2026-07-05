# Problem103
a = int(input("How many rows = "))
for i in range(a):
    print(i+1,end=' ')
    for j in range(a-i):
        print('*',end=' ')
    print('$')
