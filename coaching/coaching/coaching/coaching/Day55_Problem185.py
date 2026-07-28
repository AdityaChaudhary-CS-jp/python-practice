# Problem185
a=[]
b=[]
c=[]
row = int(input("Enter the number of rows = "))
col = int(input("Enter the number of columns = "))
print('-----------Matrix I output-----------')
for i in range(row):
    t=[]
    for j in range(col):
        k = int(input("Enter the matrix input = "))
        t.append(k)
    a.append(t)
print('-----------Matrix II output-----------')
for i in range(row):
    t=[]
    for j in range(col):
        k = int(input("Enter the matrix input = "))
        t.append(k)
    b.append(t)
print('-----------Matrix I + II output-----------')
for i in range(row):
    t=[]
    for j in range(col):
        k = a[i][j] + b[i][j]
        t.append(k)
    c.append(t)
print(a)
print(b)
print(c)
