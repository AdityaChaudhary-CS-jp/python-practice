#Problem96
a = int(input('How many rows = '))
b = int(input('How many columns = '))
for i in range(1, a + 1):
    for j in range(1, b + 1):
        if j % 2 == 1:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()
