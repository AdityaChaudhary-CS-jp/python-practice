# Problem59
a = int(input('Enter 1st Number'))
b = int(input('Enter 2nd Number'))
c = int(input('Enter 3rd Number'))

if a > b:
    if a > c:
        print("a is the greatest")
    else:
        print("c is the greatest")
else:
    if b > c:
        print("b is the greatest")
    else:
        print("c is the greatest")   
