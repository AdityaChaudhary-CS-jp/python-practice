# Problem62
a = float(input('Enter 1st Number  '))
b = float(input('Enter 2nd Number  '))
c = float(input('Enter 3rd Number  '))
if a<b and a<c :
    s=a
    if b<c:
        m=b
        g=c
    else :
        g=b
        m=c
elif b<a and b<c :
    s=b
    if a < c :
        m=a
        g=c
    else:
        g=a
        m=c
else :
    if b<a :
        g=a
        m=b
    else :
        m=a
        g=b
k = s**2
l = m**(1/3)
r = g**(1/2)
print('Square of smallest no', s,'is',k)
print('Cube root of middle no',m,'is',l)
print('Square root of greatest no',g,'is',r)
