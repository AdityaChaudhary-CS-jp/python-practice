# Problem83
x = int(input('Enter the number = '))
y = int(input('Enter the number = '))
if x>y:
    c=x
else:
    c=y
d=x*y
for i in range (c,d+1):
    if i%x==0 and i%y==0:
     l=i
     break
print('LCM',l)
