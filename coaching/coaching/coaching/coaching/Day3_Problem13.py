# Problem13
a = int(input('Enter a four digit number = '))
b = a%10
c = a//10
d = c%10
e = c//10
f = e%10
g = e//10
h = b*1000 + d*100 + f*10 + g
print('Reversed number = ',h)
