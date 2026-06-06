# Problem16
a = int(input('Enter five digit number = '))
b = a%10000
c = a//10000
d = b%1000
e = b//1000
f = d%100
g = d//100
h = f%10
i = f//10
k = g*10000 + i*1000 + h*100 + c*10 + e
print(k)
