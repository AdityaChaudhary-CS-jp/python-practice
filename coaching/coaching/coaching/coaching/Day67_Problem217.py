# Problem217
def ara(k,f):
    a =k*f
    return a
def per(p,j):
    d=2*(p+j)
    return d
l=int(input('Enter the length of rectangle = '))
b = int(input('Enter the breadth of rectangle = '))
m = ara(l,b)
q = per(l,b)
print('Area = ',m)
print('Perimeter = ',q)
