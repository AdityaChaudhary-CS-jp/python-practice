# Problem34
a = 10
b = 5
c = 20
a*=b - c  
print(a)
b%=a//b
print(b)
c-=a*b%5
print(c)
a+=c/b
print(a)
b//=a*c
print(b)
