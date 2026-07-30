# Problem192
a = int(input('Enter triangle base = '))
b = int(input('Enter triangle height = '))
c = int(input('Enter triangle side = '))
d= 0.5*a*b
e = 0.5*(a+b+c)
f = (e*(e-a)*(e-b)*(e-c))**0.5
print('Use 1/h/H for Heron\'s formula and 2/n/N for Normal formula = ',end='')
e  = input()
match e:
    case '1' | 'h' | 'H':
        print('Area of triangle = ',f)
    case '2' | 'n' | 'N':
        print('Area of triangle = ',d)
    case _:
        print('Invalid input')
