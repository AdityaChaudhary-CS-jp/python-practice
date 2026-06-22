# Problem72
a = int(input('Enter a number = '))
x = 0
y = 0
z = 1
if a==1:
    print(x)
elif a==2:
    print(x,y)
elif a==3:
    print(x,y,z)
else:
    print(x,y,z,end='  ')
    for i in range(a-3):
         k=x+y+z
         x,y,z=y,z,k
         print(k,end='  ')
