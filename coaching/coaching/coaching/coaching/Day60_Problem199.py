# Problem199
a = int(input('How many numbers = '))
b = [] 
for i in range(a):
    print('Enter',i+1,'number ',end =' ')
    c = int(input('= '))
    b.append(c)
print(b)
b.sort(reverse=True)
k=min(b)
p=b.index(k)
c=b[p-1]
l=b.index(c)
print('Third smallest Number = ',b[l-1])
