# Problem14
a = int(input('Enter a five digit number = '))
b = a%10
c = a//10
d = c%10
e = c//10
f = e%10
g = e//10
h = g%10
i = g//10
j = b*10000 + d*1000 + f*100 + h*10 + i
print('Reversed number = ',j)
