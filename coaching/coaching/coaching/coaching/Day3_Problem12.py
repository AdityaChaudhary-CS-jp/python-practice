# Problem12
a = int(input('Enter a three digit number = '))
b = a%10
c = a//10
d = c%10
e = c//10
f = b*100 + d*10 + e
print('Reversed number = ',f)
