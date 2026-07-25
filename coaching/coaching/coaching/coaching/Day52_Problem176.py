# Problem176
a=int(input('How many subject = '))
b = []
for i in range(a):
    print('Enter',i+1,'subject marks',end=' ')
    c=int(input(' = '))
    b.append(c)
s=0
for i in b:
    s=s+i
print('Total Marks Obtined = ',s)
d=s/a
print('Percentage = ',d)
if d>=90:
    print('A+ Grade')
elif d>=80:
    print('A Grade')
elif d>=70:
    print('B Grade')
elif d>=60:
    print('C Grade')
elif d>=50:
    print('D Grade')
elif d>=33:
    print('E Grade')
else:
    print('Fail')
e=b[0]
p=0
for i in range(1,len(b)):
    if b[i]<e:
        e=b[i]
        p=i+1
print('Minimum marks is = ',e)
e=b[0]
p=0
for i in range(1,len(b)):
    if b[i]>e:
        e=b[i]
        p=i+1
print('Maximum marks is = ',e)
