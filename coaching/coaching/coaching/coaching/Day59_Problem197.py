# Problem197
a = int(input('How many numbers = '))
b = [] 
for i in range(a):
    print('Enter',i+1,'number ',end =' ')
    c = int(input('= '))
    b.append(c)
print(b)
k=max(b)
d=b.count(k)
if d>1:
    p=b.index(k)
    for i in range(len(b)-1, p, -1):
        if b[i]==k:
            b.pop(i)
    print(b)
else:
    print(b)
