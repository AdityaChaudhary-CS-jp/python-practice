# Problem132
a=int(input('Enter the number = '))
k=0
p=a
m=0
l=0
o=a
while a!=0:
    r=a%10
    a=a//10
    k=k*10+r
while k!=0:
    c=k%10
    k=k//10
    l=l+1
    m=m+c**l
if o==m:
    print('Disarium Number')
else:
    print('Not Disarium Number')
