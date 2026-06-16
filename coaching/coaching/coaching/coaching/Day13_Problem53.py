# Problem53
a = int(input('Enter 1st side : '))
b = int(input('Enter 2nd side : '))
c = int(input('Enter 3rd side : '))
if a==b and a==c:
    print('Equilateral Triangle')
elif a==b or b==c or c==a :
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')
