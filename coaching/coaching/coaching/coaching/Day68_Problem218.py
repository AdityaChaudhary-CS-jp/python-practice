# Problem218
def fac(k):
    f=1
    for i in range(1,k+1):
        f=f*i
    return f
a = int(input('Enter the Value = '))
m = fac(a)
print('Factorial of',a,'is',m)
