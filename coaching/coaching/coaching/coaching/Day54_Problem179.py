# Problem179
a = int(input('How many Numbers = '))
b = []
for i in range(a):
    print('Enter',i+1,'Number',end=' ')
    c  = int(input('='))
    b.append(c)
print(b)
p =0
r =0
k =0
x =0
for i in b:
    if i%2==0:
        p=p+1
        k=k+i
    else:
        r=r+1
        x=x+i
print('Even Number = ',p)
print('Odd Number = ',r)
print('Even Number Sum = ',k)
print('Odd Number Sum = ',x)
