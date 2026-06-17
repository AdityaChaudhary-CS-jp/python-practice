# Problem57
a = int(input('Enter 1st side: '))
b = int(input('Enter 2nd side: '))
c = int(input('Enter 3rd side: '))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print('Triangle is equilateral')
    elif a == b or b == c or a == c:
        print('Triangle is isosceles')
    else:
        print('Triangle is scalene')
else:
    print('Not a triangle')
