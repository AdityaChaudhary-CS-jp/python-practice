# Problem132
a=int(input('Enter the number = '))
k=0
p=a
while a!=0:
    r=a%10
    a=a//10
    l=1
    i=1

    while i<=r:
        l=l*i
        i=i+1
    k=k+l
if p==k:
    print('Krishnamurthy number')
else:
    print('Not Krishnamurthy number')
    
