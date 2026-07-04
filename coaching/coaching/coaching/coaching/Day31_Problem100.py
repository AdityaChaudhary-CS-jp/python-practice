#Problem100
a=int(input('How many rows = '))
for i in range(a):
    for j in range(a-i):
        print('@',end=' ')
    print()
