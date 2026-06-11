# Problem40
a = int(input('Enter 1st Side of triangle : '))
b = int(input('Enter 2nd Side of triangle : '))
c = int(input('Enter 3rd Side of triangle : '))
if a==b and b==c :
    print('Equilateral Triangle')
if (a==b and b!=c) or (a!=b and b==c) or (a==c and a!=b) :
    print('Isosceles Triangle')
if a!=b and b!=c and c!=a :
    print('Scalene Triangle')
