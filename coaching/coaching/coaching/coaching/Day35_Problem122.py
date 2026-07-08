# Problem122
a=int(input('Enter the no = '))
while a!=0:
    r=a%10
    a=a//10
    k=0
    for i in range(1, r+1):
        if r % i == 0:
            k += 1
    if k == 2:
        print(r, 'is prime number')
    else:
        print(r, 'is not prime number')
