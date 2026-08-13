# Problem228
def num():
    global a,b
    a,b=b,a
a=int(input('Enter 1st number = '))
b=int(input('Enter 2nd number = '))
print(a,b)
num()
print(a,b)
