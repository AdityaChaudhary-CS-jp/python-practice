# Problem120
a=int(input('Enter the no = '))
p=a
k=0
while a!=0:
    r=a%10
    a=a//10

    k=k*10+r

if p==k:
    print('Palindrome')
else:
    print('Not Palindrome')
