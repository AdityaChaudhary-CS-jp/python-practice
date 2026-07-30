# Problem193
a = int(input('Enter the number = '))
b = []
while a!=0:
    c = a%2
    a = a//2
    b.append(c)
l =b[::-1]
print('Binary in list = ',l)
