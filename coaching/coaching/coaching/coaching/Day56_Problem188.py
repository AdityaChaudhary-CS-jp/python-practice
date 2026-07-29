# Problem188
a =[]
row = int(input('Enter number of rows = ')) 
col = int(input('Enter number of columns = '))
for i in range(row):
    t=[]
    for j in range(col):
        k=int(input('Enter matrix input = '))
        t.append(k)
    a.append(t)
for i in range(row):
    for j in range(col):
        print(a[i][j],end= '   ')
    print()
b=[]
for i in range(col):      
    t=[]
    for j in range(row):  
        t.append(0)
    b.append(t)
for i in range(row):
    for j in range(col):
        b[j][i] = a[i][j]
print('Transpose of the matrix ')
for i in range(col):    
    for j in range(row):
        print(b[i][j],end= '   ')
    print()
