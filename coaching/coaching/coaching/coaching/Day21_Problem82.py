# Problem82
x = int(input('Enter the number = '))
y = int(input('Enter the number = '))
if x>y:
    c=y
else:
    c=x
for i in range (1,c+1):
    if x%i==0 and y%i==0:
     h=i
print('HCF',h)
