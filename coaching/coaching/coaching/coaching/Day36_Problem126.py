# Problem126
a = int(input('Enter the number = '))
i = 1
m = 0
while i < a:
    if a % i == 0:
        m=m+1
    i=i+1

if m == a:
    print('Perfect number')
else:
    print('Not perfect number')
