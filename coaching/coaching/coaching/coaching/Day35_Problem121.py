# Problem121
a=int(input('Enter the no = '))
k=0
while a!=0:
    r=a%10
    a=a//10
    k=k+r
    if k%3==0:
         print(r,' is divisible by 3')
    else:
         print(r,'Not divisible by 3')
