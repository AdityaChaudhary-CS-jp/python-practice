# Problem198
a = int(input('How many numbers = '))
b = [] 
for i in range(a):
    print('Enter',i+1,'number ',end =' ')
    c = int(input('= '))
    b.append(c)
print(b)
b.sort()
k = max(b)
p = b.index(k)
print('Second greatest element = ',b[p-1])
