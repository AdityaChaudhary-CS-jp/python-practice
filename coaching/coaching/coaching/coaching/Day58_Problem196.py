# Problem196
a =int(input('How many numbers = '))
b = []
for i in range(a):
    print('Enter',i+1,'number ',end = ' ')
    c = int(input('= '))
    b.append(c)
print(b)
k = max(b)
d=b.count(k)
if d>1 :
    for i in range(d-1):
        e = b.index(k)
        b.pop(e)
    print(b)
else:
    print(b)
