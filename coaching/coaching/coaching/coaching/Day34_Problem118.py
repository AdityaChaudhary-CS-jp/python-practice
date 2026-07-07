# Problem117
a=int(input('Enter the no = '))
k=0
p=0
while a!=0:
    r=a%10
    a=a//10
    if r%2==0:
        k+=1
    else:
        p+=1
print('Odd = ',p)
print('Even = ',k)
