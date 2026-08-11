# Problem222
def mat(k,p):
    a=k+p
    b=k-p
    c=k/p
    d=k*p
    e=k%p
    f=k//p
    g=k**p
    return a,b,c,d,e,f,g
num1 = int(input('Enter First number = '))
num2 = int(input('Enter 2nd number = '))
h = mat(num1,num2)
print(h)
x,y,z,q,r,s,t=h
print(x)
print(y)
print(z)
print(q)
print(r)
print(s)
print(t)
