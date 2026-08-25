# Problem264
def stat(a,b,c):
    if a>b:
        pass
    else:
        print(a)
        a=a+c
        stat(a,b,c)
x = int(input('ENTER STARTING NUMBER = '))
y = int(input('ENTER ENDING NUMBER = '))
z = int(input('Enter gap = '))
p=stat(x,y,z)
