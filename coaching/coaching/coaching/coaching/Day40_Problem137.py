# Problem137
while True:
    l=int(input('Enter the length = '))
    b=int(input('Enter the breadth = '))
    print('1= Area \n2= Perimeter')
    c=int(input('Enter the number = '))
    if c==1:
        d =l*b
        print('Area = ',d)
    elif c==2:
        e=2*(l+b)
        print('Perimeter = ',e)
    else:
        print('Invalid')
        break
    print('---------------------------------------------------------')
