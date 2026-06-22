# Problem70
a = int(input('Enter a number = '))
x = 0
y = 1
if a==1:
    print(x)
elif a==2:
    print(x,y)
else:
    print(x,y, end= ' ')
    for i in range(a-2):
            k = x+y
            x=y
            y=k
            print(k, end = ' ')
