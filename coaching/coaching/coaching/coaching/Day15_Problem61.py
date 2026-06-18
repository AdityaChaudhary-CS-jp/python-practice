# Problem61
a = int(input('Enter 1st Number  '))
b = int(input('Enter 2nd Number  '))
c = int(input('Enter 3rd Number  '))
if a<b and a<c :
    if b<c:
        print('Ascending ', a,b,c)
    else :
        print('Ascending ', a,c,b)
elif b<a and b<c :
    if a < c :
        print('Ascending ',b,a,c )
    else:
        print('Ascending ', b,c,a)
else :
    if b<a :
        print('Ascending ', c,b,a)
    else :
        print('Ascending ', c,a,b)
