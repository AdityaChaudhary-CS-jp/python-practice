# Problem225
def ara(r,pie=3.14):
    d=pie*r**2
    print(d)
a = int(input('Enter the circle radius = '))
b = int(input('Enter 1 to enter default pie value or enter any other number for new pie value = '))
if b==1:
    ara(a)
else:
    c = int(input('Enter new pie value= '))
    ara(a,c)
