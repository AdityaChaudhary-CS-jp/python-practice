# Problem102
a = int(input("How many rows = "))
for i in range(a):
    if i == 0:
        print('5 4 3 2 1')
    else:
        for j in range(a, i, -1):
            print(j, end=" ")
        print()
