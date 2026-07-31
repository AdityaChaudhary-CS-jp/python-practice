# Problem195
a = input('Enter the binary = ')
b = list(a)
b.reverse()
k = 0
for i in range(len(b)):
    k = k + int(b[i])*2**i
print('Number = ', k)
