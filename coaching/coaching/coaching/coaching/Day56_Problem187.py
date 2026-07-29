# Problem187
a = []  
row = int(input('Enter number of rows = '))
col = int(input('Enter number of columns = '))  
for i in range(row):
    t=[]
    for j in range(col):
        k=int(input('Enter matrix input = '))
        t.append(k)
    a.append(t) 
print('MATRIX OUTPUT')
for i in range(row):
    for j in range(col):
        print(a[i][j],end= '   ')
    print()
c = int(input('Enter any number to search in matrix = '))
f = 0

for i in range(row):
    for j in range(col):
        if a[i][j] == c:
            print('Number Found In Matrix')
            print('Row number =', i+1)
            print('Column number =', j+1)
            f = 1
            break
    if f == 1:
        break

if f == 0:
    print('Number Not Found In Matrix')
