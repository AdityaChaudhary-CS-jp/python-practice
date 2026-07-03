#Problem90
a = int(input('How many rows = '))
b = int(input('How many column = '))
num = 1
for i in range(a):
    for j in range(b):
        print(num, end=' ')
        num += 1
    print()
