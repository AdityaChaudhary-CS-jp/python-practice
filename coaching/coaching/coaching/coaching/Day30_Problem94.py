# Problem94
a = int(input('How many rows = '))
b = int(input('How many column = '))
for i in range(a):
    for j in range(b):
        k = ord('a') + j
        print(chr(k), end=' ')
    print()
