# Problem28
a = int(input('Enter the number = '))
b = int(input('Enter the number = '))
print(a,b)
a,b = b,a
print(a,b)
# OR
a = int(input('Enter the number = '))
b = int(input('Enter the number = '))
print(a,b)
k = a
a = b
b = k
print(a,b)
# OR
a = int(input('Enter the number = '))
b = int(input('Enter the number = '))
print(a,b)
a = a + b
b = a - b
a = a - b
print(a,b)
