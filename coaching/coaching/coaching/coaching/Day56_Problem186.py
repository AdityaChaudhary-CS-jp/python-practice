# Problem186
a = []
c = int(input('Enter order of the matrix = '))
for i in range(c):
    t = []
    for j in range(c):
        k = int(input('Enter matrix input = '))
        t.append(k)
    a.append(t)
print('SQUARE MATRIX')
for i in range(c):
    for j in range(c):
        print(a[i][j],end= '   ')
    print()
d = int(input('Enter any row number = '))
l = int(input('Enter any column number = '))    
p=0
for k in range(c):
    p=p+a[d-1][k]
print('Sum of row', d, 'is', p)
m=0
for k in range(c):
    m=m+a[k][l-1]
print('Sum of column', l, 'is', m)
o=0
for k in range(c):
    o=o+a[k][k]
print('Sum of diagonal is', o)
