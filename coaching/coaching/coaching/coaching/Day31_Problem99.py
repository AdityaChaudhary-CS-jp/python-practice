#Problem99
a=int(input('How many rows = '))
for i in range(1, a+1):
    for j in range(i):
        k = ord('a') +j
        print(chr(k), end=' ')
    print()
